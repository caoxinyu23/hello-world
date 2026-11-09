# 中文字体回退层（由移植流水线添加，不属于原版游戏）
#
# 原作所有文字都用 fonts/Tox Typewriter.ttf —— 那是一款打字机风格的拉丁字体，
# 没有任何 CJK 字形。结果是：
#   * 偏好设置里那个 textbutton "中文" 渲染成一片空白（看起来像"没有中文选项"）
#   * 即使切到中文，正文也全是空白/方框
#
# 这里用 Ren'Py 的 FontGroup 做分层回退：
#   拉丁字母、西语重音符、标点  → 仍然用 Tox Typewriter（保持原作观感）
#   中日韩字符                → 落到 DroidSansFallback（Apache-2.0，可随包分发）
#
# 字体选型：用单文件 TrueType（glyf）而不是 .ttc 集合。Ren'Py 虽然支持
# "index@路径" 指定集合里的 face，但 CFF 型 .ttc 在部分 FreeType/SDL_ttf 路径上
# 会加载失败（实测主菜单渲染即报错）。DroidSansFallback 是普通 TrueType，
# 覆盖 CJK，Apache-2.0 许可，零格式风险。
#
# 不做预加载检查：init 阶段显示系统还没起来，试加载会误报失败。真加载发生在
# 首次渲染时，有问题会在画面上直接暴露，而不是被这里悄悄降级。

init -1 python:

    from renpy.text.font import FontGroup

    _latin_font = "fonts/Tox Typewriter.ttf"
    _cjk_font = "fonts/DroidSansFallback.ttf"

    _game_font = FontGroup()
    _game_font.add(_latin_font, 0x0020, 0x2E7F)
    _game_font.add(_cjk_font, 0x2E80, 0xFFFF)
