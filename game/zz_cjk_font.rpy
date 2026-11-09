# 中文字体回退层（由移植流水线添加，不属于原版游戏）
#
# 原作所有文字都用 fonts/Tox Typewriter.ttf —— 那是一款打字机风格的拉丁字体，
# 没有任何 CJK 字形。结果是：
#   * 偏好设置里那个 textbutton "中文" 渲染成一片空白（看起来像"没有中文选项"）
#   * 即使切到中文，正文也全是空白/方框
#
# 这里用 Ren'Py 的 FontGroup 做分层回退：
#   拉丁字母、西语重音符、标点  → 仍然用 Tox Typewriter（保持原作观感）
#   中日韩字符                → 落到 Noto Sans CJK（OFL 许可，可随包分发）
#
# 注意 NotoSansCJK 是 .ttc 字体集合，Ren'Py 用 "index@路径" 指定第几个 face，
# 所以写 "0@fonts/NotoSansCJK-Regular.ttc"。
#
# 不做预加载检查：init 阶段显示系统还没起来，试加载会误报失败。真加载发生在
# 首次渲染时，有问题会在画面上直接暴露，而不是被这里悄悄降级。

init -1 python:

    from renpy.text.font import FontGroup

    _latin_font = "fonts/Tox Typewriter.ttf"
    _cjk_font = "0@fonts/NotoSansCJK-Regular.ttc"

    _game_font = FontGroup()
    _game_font.add(_latin_font, 0x0020, 0x2E7F)
    _game_font.add(_cjk_font, 0x2E80, 0xFFFF)
