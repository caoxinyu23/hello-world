# Android 兼容层（由移植流水线添加，原始的 .rpy 文件一行未改）
#
# 原作是 Windows/macOS/Linux 桌面游戏，其中三处"第四面墙"机制直接调用桌面 API：
#   rutas/memorias.rpy  → subprocess.Popen(['xdg-open', carpeta])
#   rutas/pantallas.rpy → subprocess.Popen(['xdg-open', ruta])   (abrir_imagen)
#   rutas/pantallas.rpy → subprocess.Popen(['xdg-open', carpeta]) (abrir_carpeta)
# Android 上不存在 xdg-open/open 可执行文件，Popen 会抛 FileNotFoundError，
# Ren'Py 会把交互中断在异常界面（游戏卡死）。
#
# 处理方式：把游戏对 Popen 的调用做"哑火"处理，并补上一个非空的用户名
# （原作 init 阶段读 os.getenv('USERNAME')/USER，Android 上为空，会让
# "tú debes ser [usuario]" 这句台词变成空白）。
#
# 注意：blocklist.txt 会把 **.rpy 排除出 APK，只打包 .rpyc，
# 所以 CI 必须先用 `renpy.sh <project> compile` 编译，本文件才会生效。

init -1 python:
    import os as _android_os

    if renpy.android:
        # 桌面目录不存在时会走 os.makedirs，这里给 HOME 一个可写落点，
        # 让原作写 "Corazón.txt / Instrucciones.txt" 的逻辑不至于抛异常。
        _android_os.environ.setdefault("HOME", _android_os.getcwd())
        _android_os.environ.setdefault("USER", "el visitante")
        _android_os.environ.setdefault("USERNAME", "el visitante")

init -1 python:
    import subprocess as _android_subprocess

    if renpy.android and not getattr(_android_subprocess, "_renpy_android_patched", False):

        _AndroidPopen = _android_subprocess.Popen

        class _NoOpPopen(object):
            """Popen 替身：外部程序不存在时静默失败，而不是中断剧情。"""

            def __init__(self, args, *a, **kw):
                self.args = args
                self.proc = None
                try:
                    self.proc = _AndroidPopen(args, *a, **kw)
                except Exception:
                    try:
                        renpy.notify(
                            "Android: no hay visor externo de archivos. "
                            "El archivo se guardó en los datos de la app."
                        )
                    except Exception:
                        pass

            def __getattr__(self, name):
                raise AttributeError("_NoOpPopen has no attribute %r" % (name,))

        _android_subprocess.Popen = _NoOpPopen
        _android_subprocess._renpy_android_patched = True
