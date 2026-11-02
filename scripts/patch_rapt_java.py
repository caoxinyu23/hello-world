#!/usr/bin/env python3
"""
在 RAPT 的 PythonSDLActivity.preparePython() 里插入诊断日志：
打印 getFilesDir() 的清单（有没有 main.py）以及 ANDROID_PRIVATE / ANDROID_PUBLIC
到底有没有被设进进程环境。

为什么需要：librenpython.so 里的 start_python 会去 <ANDROID_PRIVATE>/main.py 跑入口。
如果那个文件不存在、或者环境变量没传下来，它会静默返回（Python 的 stderr 在
Android 上被丢弃），表现就是"Activity 起来了、30ms 后自己退出、什么都不发生"。

用法: patch_rapt_java.py <sdk>/rapt
"""

import os
import sys

MARK = "PRIVFILES count="

SNIPPET = '''
        // === injected diagnostics (harmless in release) ===
        try {
            java.io.File _priv = getFilesDir();
            java.io.File[] _pf = _priv.listFiles();
            Log.v("python", "DGFILES count=" + (_pf == null ? -1 : _pf.length) + " dir=" + _priv);
            if (_pf != null) {
                for (int _i = 0; _i < _pf.length && _i < 40; _i++) {
                    Log.v("python", "DGFILE " + _pf[_i].getName() + " size=" + _pf[_i].length());
                }
            }
            Log.v("python", "DGENV ANDROID_PRIVATE=" + System.getenv("ANDROID_PRIVATE")
                    + " ANDROID_PUBLIC=" + System.getenv("ANDROID_PUBLIC"));
        } catch (Throwable _t) {
            Log.v("python", "DGCHK failed " + _t);
        }

        // === end injected diagnostics ===
'''


def patch(java_path):
    src = open(java_path, encoding="utf-8").read()
    if "DGFILES count=" in src:
        print("已注入过: %s" % java_path)
        return False

    anchor = 'Log.v("python", "Finished preparePython.");'
    if anchor not in src:
        raise SystemExit("找不到注入点（preparePython 的日志行）: %s" % java_path)

    src = src.replace(anchor, anchor + "\n" + SNIPPET, 1)
    open(java_path, "w", encoding="utf-8").write(src)
    print("已注入诊断: %s" % java_path)
    return True


def main():
    rapt = sys.argv[1] if len(sys.argv) > 1 else None
    if not rapt or not os.path.isdir(rapt):
        raise SystemExit("用法: patch_rapt_java.py <sdk>/rapt")

    rel = "prototype/renpyandroid/src/main/java/org/renpy/android/PythonSDLActivity.java"
    n = 0
    for base in ("prototype", "project"):
        p = os.path.join(rapt, base, "renpyandroid/src/main/java/org/renpy/android/PythonSDLActivity.java")
        if os.path.exists(p) and patch(p):
            n += 1
    if n == 0 and not os.path.exists(os.path.join(rapt, rel)):
        raise SystemExit("RAPT 里没有 PythonSDLActivity.java，路径可能变了")
    print("完成，改动文件数: %d" % n)


if __name__ == "__main__":
    main()
