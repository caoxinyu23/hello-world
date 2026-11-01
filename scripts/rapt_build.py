#!/usr/bin/env python3
"""
Headless RAPT driver for GitHub Actions.

This calls Ren'Py's Android packaging tool (rapt) directly instead of
    renpy.sh launcher android_build <project>
because the launcher path needs a display, a project model and runs the game
(`Project.update_dump`) before packaging. Everything done here is exactly what
the launcher would do, just without the GUI:

  1. rapt/sdk.txt          -> points rapt at the Android SDK
  2. <base>/android.keystore -> signing key (alias "android", pass "android",
                               which is what rapt's update_project_keys writes
                               into project/local.properties)
  3. <dist>/android.json   -> Application configuration (package, name, ...)
  4. <dist>/               -> a "built Ren'Py game" layout that rapt splits into
                              private assets (renpy/ + main.py) and game assets
  5. rapt.build.build()    -> renders the gradle project, runs assembleRelease

Environment:
  RENPY_SDK   Ren'Py SDK root (contains renpy/, rapt/, lib/py3-linux-x86_64)
  PROJ        repo root (base dir for android.keystore; holds ToEataGod.py)
  GAME_DIR    game/ directory to package (the compiled one)
  DIST        scratch dir, will be created/emptied
  OUT_DIR     where to copy the resulting .apk
"""

import glob
import hashlib
import json
import os
import shutil
import subprocess
import sys

RENPY_SDK = os.environ["RENPY_SDK"]
PROJ = os.path.abspath(os.environ["PROJ"])
GAME_DIR = os.path.abspath(os.environ["GAME_DIR"])
DIST = os.path.abspath(os.environ["DIST"])
OUT_DIR = os.path.abspath(os.environ.get("OUT_DIR", os.path.join(PROJ, "out")))

# 可选覆盖：冒烟包用 android.smoke.json + 独立包名，可和正式包共存
ANDROID_JSON = os.path.abspath(os.environ.get("ANDROID_JSON") or os.path.join(PROJ, "android.json"))
MAIN_PY = os.path.abspath(os.environ.get("MAIN_PY") or os.path.join(PROJ, "ToEataGod.py"))

# PROBE_MAIN=1：往 main.py 顶部注入 stderr 重定向和 traceback 探针，
# 把 Python 侧的错误写到 <外部私有目录>/py-probe.log 与 py-stderr.txt。
# Android 上 python 的 stderr 默认被丢弃，没有这个探针就完全看不到异常。
PROBE_MAIN = os.environ.get("PROBE_MAIN") == "1"

PROBE_HEAD = '''# === probe injected by CI (PROBE_MAIN=1) ===
import os as _probe_os, sys as _probe_sys, traceback as _probe_tb
def _probe(msg):
    try:
        _d = _probe_os.environ.get("ANDROID_PUBLIC") or "/data/local/tmp"
        with open(_probe_os.path.join(_d, "py-probe.log"), "a") as _f:
            _f.write(msg + "\\n")
    except Exception:
        pass
_probe("main.py begin name=%r argv=%r cwd=%r priv=%r pub=%r" % (
    __name__, _probe_sys.argv, _probe_os.getcwd(),
    _probe_os.environ.get("ANDROID_PRIVATE"), _probe_os.environ.get("ANDROID_PUBLIC")))
try:
    _pd = _probe_os.environ.get("ANDROID_PUBLIC")
    if _pd:
        _probe_sys.stderr = _probe_sys.stdout = open(
            _probe_os.path.join(_pd, "py-stderr.txt"), "a", buffering=1)
        _probe("stderr redirected")
except Exception as _pe:
    _probe("stderr redirect failed: %r" % (_pe,))
# === end probe ===
'''

PROBE_TAIL_OLD = 'if __name__ == "__main__":\n    main()'

PROBE_TAIL_NEW = '''if __name__ == "__main__":
    try:
        _probe("calling main()")
        main()
        _probe("main() returned normally")
    except SystemExit as _se:
        _probe("SystemExit: %r" % (_se,))
        raise
    except BaseException:
        _probe("EXCEPTION:\\n" + _probe_tb.format_exc())
        raise
'''

KEYSTORE_PASS = "android"   # rapt hardcodes this in local.properties
KEY_ALIAS = "android"       # ditto


def log(msg):
    print("\n=== %s ===" % msg, flush=True)


def run(*args, **kw):
    print("+ " + " ".join(args), flush=True)
    subprocess.check_call(args, **kw)


def check_toolchain():
    """Fail fast, with a clear message, before doing any heavy work."""

    android_home = os.environ.get("ANDROID_HOME") or os.environ.get("ANDROID_SDK_ROOT")
    if not android_home or not os.path.isdir(android_home):
        sys.exit("ANDROID_HOME is not set / does not exist: %r" % (android_home,))

    for rel in ("platforms/android-36", "build-tools/36.0.0", "cmdline-tools/latest"):
        if not os.path.isdir(os.path.join(android_home, rel)):
            sys.exit("Android SDK is missing %s under %s" % (rel, android_home))

    for rel in ("renpy/__init__.py", "rapt/buildlib/rapt/build.py",
                "lib/py3-linux-x86_64/python"):
        if not os.path.exists(os.path.join(RENPY_SDK, rel)):
            sys.exit("Ren'Py SDK looks incomplete, missing %s under %s" % (rel, RENPY_SDK))

    if not shutil.which("keytool"):
        sys.exit("keytool not found (needs a JDK on PATH)")

    log("toolchain")
    print("ANDROID_HOME = %s" % android_home)
    print("RENPY_SDK    = %s" % RENPY_SDK)
    print("GAME_DIR     = %s" % GAME_DIR)
    print("DIST         = %s" % DIST)


def write_sdk_txt():
    """rapt reads the SDK location from rapt/sdk.txt (or rapt/Sdk)."""

    android_home = os.environ.get("ANDROID_HOME") or os.environ.get("ANDROID_SDK_ROOT")
    target = os.path.join(RENPY_SDK, "rapt", "sdk.txt")
    with open(target, "w") as f:
        f.write(android_home.strip() + "\n")
    print("wrote %s -> %s" % (target, android_home.strip()))


def keystore_ok(ks):
    """A usable keystore must open with storepass 'android' and hold alias 'android'."""

    try:
        r = subprocess.run(
            ["keytool", "-list", "-keystore", ks, "-storepass", KEYSTORE_PASS,
             "-alias", KEY_ALIAS],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        return r.returncode == 0
    except OSError:
        return False


def ensure_keystore():
    """rapt signs with <base>/android.keystore, alias/android, pass android."""

    ks = os.path.join(PROJ, "android.keystore")

    if os.path.exists(ks):
        if keystore_ok(ks):
            print("reusing existing keystore %s" % ks)
            return ks
        print("WARNING: %s exists but is not a usable keystore, regenerating" % ks)
        os.unlink(ks)

    run(
        "keytool", "-genkeypair",
        "-keystore", ks,
        "-alias", KEY_ALIAS,
        "-keyalg", "RSA",
        "-keysize", "2048",
        "-validity", "20000",
        "-storepass", KEYSTORE_PASS,
        "-keypass", KEYSTORE_PASS,
        "-dname", "CN=ToEataGod port,O=Port,C=CN",
    )
    print("generated %s (ephemeral: a new key means a new signature)" % ks)
    return ks


def build_dist():
    """Assemble the tree rapt.build.build() expects inside <dist>."""

    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    # rapt's split_renpy() requires <dist>/renpy/common and <dist>/game.
    game_dst = os.path.join(DIST, "game")
    renpy_dst = os.path.join(DIST, "renpy")

    # Hardlink when possible: 740 MB of assets, and rapt only moves/renames
    # directory entries at this level. Fall back to a real copy when the
    # filesystem refuses hardlinks (e.g. FUSE mounts).
    if subprocess.call(["cp", "-al", GAME_DIR, game_dst]) != 0:
        print("hardlink copy failed, falling back to a full copy")
        if os.path.exists(game_dst):
            shutil.rmtree(game_dst)
        shutil.copytree(GAME_DIR, game_dst)

    shutil.copytree(os.path.join(PROJ, "renpy"), renpy_dst)

    # split_renpy() moves <dist>/*.py to private/main.py; the PC build ships
    # one launcher script, that is exactly what is needed here.
    main_dst = os.path.join(DIST, "ToEataGod.py")
    shutil.copy2(MAIN_PY, main_dst)

    if PROBE_MAIN:
        text = open(main_dst, encoding="utf-8").read()
        if PROBE_TAIL_OLD in text:
            text = text.replace(PROBE_TAIL_OLD, PROBE_TAIL_NEW)
        else:
            text += "\n\n" + PROBE_TAIL_NEW
        text = PROBE_HEAD + "\n" + text
        open(main_dst, "w", encoding="utf-8").write(text)
        print("probe 已注入 main.py (%d 字节)" % len(text))

    # The PC runtime libraries (lib/, 103 MB) are useless on Android:
    # librenpython.so already embeds CPython. Provide an empty lib/ so
    # split_renpy() has something to move into private/.
    os.makedirs(os.path.join(DIST, "lib"), exist_ok=True)

    # rapt.configuration.Configuration(directory) reads android.json from the
    # directory it is handed, i.e. from <dist>, not from the repo root.
    shutil.copy2(ANDROID_JSON, os.path.join(DIST, "android.json"))
    print("android.json <- %s" % ANDROID_JSON)

    if not os.path.isdir(os.path.join(renpy_dst, "common")):
        sys.exit("renpy/common is missing; rapt cannot split the game tree")

    print("dist ready: %s" % DIST)


def main():
    check_toolchain()
    write_sdk_txt()
    ensure_keystore()
    build_dist()

    # Import only after sdk.txt exists: rapt.plat resolves the SDK at import time.
    sys.path.insert(0, RENPY_SDK)
    sys.path.insert(0, os.path.join(RENPY_SDK, "rapt", "buildlib"))

    import rapt.interface as interface
    import rapt.build as build
    import rapt.plat as plat

    log("rapt")
    print("RAPT_PATH = %s" % plat.RAPT_PATH)
    print("sdk       = %s" % plat.sdk)
    print("gradlew   = %s" % plat.gradlew)

    iface = interface.Interface()

    produced = []

    def finished(files):
        produced.extend(files)

    try:
        build.build(
            iface,
            DIST,
            PROJ,
            bundle=False,
            install=False,
            launch=False,
            finished=finished,
        )
    except SystemExit:
        raise
    except Exception:
        import traceback
        traceback.print_exc()
        sys.exit("rapt build raised an exception (see traceback above)")

    # rapt copies results into rapt/bin/ as well as into `files`.
    apks = sorted(set(produced) | set(glob.glob(plat.path("bin/*.apk"))))
    if not apks:
        sys.exit("build finished but no .apk was found in %s" % plat.path("bin"))

    os.makedirs(OUT_DIR, exist_ok=True)

    log("artifacts")
    for i in apks:
        dst = os.path.join(OUT_DIR, os.path.basename(i))
        shutil.copy2(i, dst)
        h = hashlib.sha256()
        with open(dst, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        print("%s\n  %d bytes\n  sha256 %s" % (dst, os.path.getsize(dst), h.hexdigest()))


if __name__ == "__main__":
    main()
