#!/usr/bin/env bash
# 从一份 PC 发行版重新铺 game/ + renpy/ + ToEataGod.py（游戏换版本时用）。
#
#   ./scripts/make-payload.sh /path/to/ToEataGod-3.0-pc/ToEataGod-3.0-pc
#
# 只复制 RAPT 真正需要的东西：game/、renpy/、那个 .py 启动脚本。
# lib/（PC 版 CPython）、.exe、.sh 都不进仓库。
set -euo pipefail

SRC="${1:?用法: make-payload.sh <PC 发行版根目录>}"
SRC="$(cd "$SRC" && pwd)"
DEST="$(cd "$(dirname "$0")/.." && pwd)"

[ -d "$SRC/game" ]  || { echo "找不到 $SRC/game"; exit 1; }
[ -d "$SRC/renpy" ] || { echo "找不到 $SRC/renpy"; exit 1; }

LAUNCHER=$(find "$SRC" -maxdepth 1 -name '*.py' | head -n1)
[ -n "$LAUNCHER" ] || { echo "$SRC 下没有 .py 启动脚本"; exit 1; }

echo "源:     $SRC"
echo "目标:   $DEST"
echo "启动器: $(basename "$LAUNCHER")"

rm -rf "$DEST/game" "$DEST/renpy"
cp -a "$SRC/game"  "$DEST/game"
cp -a "$SRC/renpy" "$DEST/renpy"
cp -a "$LAUNCHER"  "$DEST/$(basename "$LAUNCHER")"

# 兼容层必须在覆盖之后补回来（它不属于原始发行版）
if [ ! -f "$DEST/game/android_compat.rpy" ]; then
    echo "警告: game/android_compat.rpy 不见了，Android 上会卡在 xdg-open 那三处" >&2
fi

echo "--- 结果 ---"
du -sh "$DEST/game" "$DEST/renpy"
find "$DEST/game" -type f | wc -l
