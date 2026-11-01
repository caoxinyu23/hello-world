#!/usr/bin/env python3
"""
生成一个"冒烟"游戏目录：和真实游戏同一套引擎/GUI/流水线，但没有 740 MB 资源，
打出来的 APK 只有 ~45 MB（几乎全是 librenpython.so），用来快速区分

    A. 流水线/配置本身有问题      -> 冒烟包也一样闪退
    B. 真实游戏内容有问题        -> 冒烟包能跑

用法: make_smoke_game.py <repo_game_dir> <out_dir>
"""

import os
import re
import shutil
import sys

REPO_GAME = os.path.abspath(sys.argv[1])
OUT = os.path.abspath(sys.argv[2])

# 必须带的：GUI 定义、界面脚本、中文字体（不影响，但保持与正式包一致）、
# 以及 gui/ 目录里的按钮/滑块贴图（screens.rpy 会用到）。
COPY = [
    "gui.rpy",
    "screens.rpy",
    "glitch_tag.rpy",
    "kinetic_text_tags.rpy",
]
COPY_DIRS = ["gui", "fonts"]

SCRIPT = """\
# 冒烟测试用脚本：不依赖任何图片/音频资源
define probe = Character("Probe", color="#ffffff")

label start:
    probe "smoke ok: Ren'Py 起来了。"
    "如果你的手机看到这句，说明流水线、包结构、引擎启动都是好的。"
    return
"""

OPTIONS = """\
define config.name = _("ToEataGod SMOKE")
define config.version = "3.0"
define build.name = "ToEataGodSmoke"
define config.save_directory = "toeatagod-smoke"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.window = "auto"
define config.window_icon = "gui/window_icon.png"

define config.enter_transition = dissolve
define config.exit_transition = dissolve
"""


def main():

    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    for fn in COPY:
        src = os.path.join(REPO_GAME, fn)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(OUT, fn))
        else:
            print("WARN: 缺少 %s" % fn)

    for dn in COPY_DIRS:
        src = os.path.join(REPO_GAME, dn)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(OUT, dn))
        else:
            print("WARN: 缺少目录 %s" % dn)

    # 真实 gui.rpy 的主菜单背景指向 images/main_menu_null.webm，
    # 冒烟包里没有 images/，换成纯色，否则主菜单会报缺资源。
    gui = os.path.join(OUT, "gui.rpy")
    if os.path.exists(gui):
        text = open(gui, encoding="utf-8").read()
        text, n = re.subn(
            r'define gui\.main_menu_background\s*=\s*Movie\s*\(play="images/main_menu_null\.webm"\)',
            'define gui.main_menu_background = Solid("#7a1010")',
            text,
        )
        open(gui, "w", encoding="utf-8").write(text)
        print("gui.rpy 主菜单背景已替换为纯色 (匹配 %d 处)" % n)

    open(os.path.join(OUT, "script.rpy"), "w", encoding="utf-8").write(SCRIPT)
    open(os.path.join(OUT, "options.rpy"), "w", encoding="utf-8").write(OPTIONS)

    total = 0
    for dp, _, fns in os.walk(OUT):
        for fn in fns:
            total += os.path.getsize(os.path.join(dp, fn))

    print("冒烟游戏目录: %s" % OUT)
    print("文件数: %d, 体积: %.1f MB" % (
        sum(len(f) for _, _, f in os.walk(OUT)), total / 1048576))


if __name__ == "__main__":
    main()
