#!/usr/bin/env python3
"""生成 tl/chino 下的界面翻译文件（screens / options / glitch_tag / kinetic_text_tags）。

只替换 new 值，old 值（西语/英语原文）必须逐字符保留，否则 Ren'Py 匹配不上。
"""
import os
import re
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "game", "tl", "ingles")
DST = os.path.join(ROOT, "game", "tl", "chino")
os.makedirs(os.path.join(DST, "rutas"), exist_ok=True)

# ---------------------------------------------------------------- screens.rpy
# key = 英文 new 值（原始文本，\n 表示反斜杠+n 两个字符）
# value = 中文译文
ZH = {
    "Back": "返回",
    "History": "历史",
    "Skip": "跳过",
    "Auto": "自动",
    "Save": "存档",
    "Q.Save": "快速存档",
    "Q.Load": "快速读档",
    "Prefs": "设置",
    "Start": "开始",
    "Load": "读取",
    "Preferences": "偏好设置",
    "End Replay": "结束回放",
    "Main Menu": "主菜单",
    "About": "关于",
    "Help": "帮助",
    "Quit": "退出",
    "Return": "返回",
    "Version [config.version!t]\\n": "版本 [config.version!t]\\n",
    "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\\n\\n[renpy.license!t]":
        "使用 {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only] 制作。\\n\\n[renpy.license!t]",
    "Game made by Soffis_mbm / {a=https://twitter.com/Mardonesa_soffi}Mardonesa_soffi on Twitter{/a} with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\\n\\n[renpy.license!t]":
        "本游戏由 Soffis_mbm / {a=https://twitter.com/Mardonesa_soffi}Mardonesa_soffi{/a} 制作，"
        "使用 {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]。\\n\\n[renpy.license!t]",
    "Page {}": "第 {} 页",
    "Automatic saves": "自动存档",
    "Quick saves": "快速存档",
    "{#file_time}%A, %B %d %Y, %H:%M": "{#file_time}%Y年%m月%d日 %H:%M",
    "empty slot": "空槽位",
    "<": "<",
    "{#auto_page}A": "{#auto_page}A",
    "{#quick_page}Q": "{#quick_page}Q",
    ">": ">",
    "Upload Sync": "上传同步",
    "Download Sync": "下载同步",
    "Display": "显示",
    "Window": "窗口",
    "Fullscreen": "全屏",
    "Unseen Text": "未读文本",
    "After Choices": "选项之后",
    "Transitions": "过渡",
    "Language": "语言",
    "Text Speed": "文字速度",
    "Auto-Forward Time": "自动前进时长",
    "Music Volume": "音乐音量",
    "Sound Volume": "音效音量",
    "Test": "测试",
    "Voice Volume": "语音音量",
    "Mute All": "全部静音",
    "The dialogue history is empty.": "对话历史为空。",
    "Keyboard": "键盘",
    "Mouse": "鼠标",
    "Gamepad": "手柄",
    "Enter": "回车",
    "Advances dialogue and activates the interface.": "推进对话并激活界面。",
    "Space": "空格",
    "Advances dialogue without selecting choices.": "不选择选项即可推进对话。",
    "Arrow Keys": "方向键",
    "Navigate the interface.": "导航界面。",
    "Escape": "Esc",
    "Accesses the game menu.": "打开游戏菜单。",
    "Ctrl": "Ctrl",
    "Skips dialogue while held down.": "按住时跳过对话。",
    "Tab": "Tab",
    "Toggles dialogue skipping.": "切换对话跳过。",
    "Page Up": "上一页",
    "Rolls back to earlier dialogue.": "回滚到之前的对话。",
    "Page Down": "下一页",
    "Rolls forward to later dialogue.": "前进到之后的对话。",
    "Hides the user interface.": "隐藏用户界面。",
    "Takes a screenshot.": "截图。",
    "Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.":
        "切换辅助{a=https://www.renpy.org/l/voicing}自我朗读{/a}。",
    "Opens the accessibility menu.": "打开辅助功能菜单。",
    "Left Click": "左键点击",
    "Middle Click": "中键点击",
    "Right Click": "右键点击",
    "Mouse Wheel Up\\nClick Rollback Side": "鼠标滚轮上\\n点击回滚侧",
    "Mouse Wheel Down": "鼠标滚轮下",
    "Right Trigger\\nA/Bottom Button": "右扳机\\nA/底部按键",
    "Left Trigger\\nLeft Shoulder": "左扳机\\n左肩键",
    "Right Shoulder": "右肩键",
    "D-Pad, Sticks": "方向键、摇杆",
    "Start, Guide": "Start、Guide",
    "Y/Top Button": "Y/顶部按键",
    "Calibrate": "校准",
    "Yes.": "是。",
    "No.": "否。",
    "Skipping": "跳过中",
    "Menu": "菜单",
    "Enter your name.": "输入你的名字。",
    "Another Story": "另一个故事",
}

# 两条带署名的长 credits：old 保留，new 改成中文
CREDITS_NEW = (
    "本游戏由 Soffis_mbm / {a=https://twitter.com/Mardonesa_soffi}Mardonesa_soffi{/a} 制作，"
    "英文校译感谢：{b}A bunny <3{b}。"
    "使用 {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]。\\n\\n[renpy.license!t]"
)
CREDITS_FULL_NEW = "版本 [config.version!t]\\n" + CREDITS_NEW

# old 里含 "and corrected english translation thanks to" 的两条
CREDITS_OLD_MARK = "and corrected english translation thanks to"

NEW_LINE_RE = re.compile(r'^(?P<indent>\s*)new\s+"(?P<text>.*)"(?P<trailer>\s*#.*)?$')


def translate_screens():
    src = os.path.join(SRC, "screens.rpy")
    out = []
    n = 0
    miss = []
    for line in open(src, encoding="utf-8", errors="ignore"):
        m = NEW_LINE_RE.match(line.rstrip("\n"))
        if m:
            raw = m.group("text")
            if CREDITS_OLD_MARK in raw or raw.startswith("Version [config.version!t]"):
                # 署名长串
                if raw.startswith("Version [config.version!t]"):
                    zh = CREDITS_FULL_NEW
                else:
                    zh = CREDITS_NEW
            else:
                zh = ZH.get(raw)
                if zh is None:
                    miss.append(raw)
                    zh = raw
            out.append(f'{m.group("indent")}new "{zh}"{m.group("trailer") or ""}\n')
            n += 1
        else:
            out.append(line)
    out = [l.replace("translate ingles ", "translate chino ", 1) if l.startswith("translate ingles ") else l for l in out]
    dest = os.path.join(DST, "screens.rpy")
    with open(dest, "w", encoding="utf-8") as fh:
        fh.writelines(out)
    print(f"screens.rpy: 翻译 {n} 条，未覆盖 {len(miss)} 条")
    for x in miss:
        print("   MISS:", x[:100])


def translate_simple(name, mapping):
    src = os.path.join(SRC, name)
    out = []
    n = 0
    for line in open(src, encoding="utf-8", errors="ignore"):
        m = NEW_LINE_RE.match(line.rstrip("\n"))
        if m:
            raw = m.group("text")
            zh = mapping.get(raw, raw)
            out.append(f'{m.group("indent")}new "{zh}"{m.group("trailer") or ""}\n')
            n += 1
        else:
            out.append(line)
    out = [l.replace("translate ingles ", "translate chino ", 1) if l.startswith("translate ingles ") else l for l in out]
    dest = os.path.join(DST, name)
    with open(dest, "w", encoding="utf-8") as fh:
        fh.writelines(out)
    print(f"{name}: 翻译 {n} 条")


if __name__ == "__main__":
    translate_screens()
    translate_simple("options.rpy", {
        "To eat a god": "吞噬神明",
        "To Eat a God": "吞噬神明",
    })
    translate_simple("glitch_tag.rpy", {
        # 模块署名，保留原文即可
    })
    translate_simple("kinetic_text_tags.rpy", {})
