#!/usr/bin/env python3
"""轻量汉化流水线：子代理只输出 zh 数组，本脚本负责合并。

子代理读 <name>.src.json（含 line/es/text），输出 <name>.zh.json
（[{"line":N,"zh":"..."}]）。本脚本按 line 合并进 <name>.done.json。

用法：
  python3 chino_light.py prepare <name> [<name>...]   # 生成 .src.json
  python3 chino_light.py merge <name> [<name>...]     # 合并 .zh.json
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITEMS = os.path.join(ROOT, ".build", "chino_items")


def src_path(name):
    return os.path.join(ITEMS, name + ".json")


def prepare(name):
    src = src_path(name)
    if not os.path.exists(src):
        print(f"!! 源文件不存在: {src}")
        return False
    done = os.path.join(ITEMS, name + ".done.json")
    if os.path.exists(done):
        print(f"跳过（已 done）: {name}")
        return True
    items = json.load(open(src, encoding="utf-8"))
    compact = [
        {"line": it["line"], "es": it.get("es", ""), "text": it.get("text", "")}
        for it in items
    ]
    out = os.path.join(ITEMS, name + ".src.json")
    json.dump(compact, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"生成 {len(compact)} 条 -> {os.path.basename(out)}")
    return True


def merge(name):
    src = src_path(name)
    done = os.path.join(ITEMS, name + ".done.json")
    zhf = os.path.join(ITEMS, name + ".zh.json")
    if os.path.exists(done):
        print(f"跳过（已 done）: {name}")
        return True
    if not os.path.exists(zhf):
        print(f"缺少 zh: {name}")
        return False
    items = json.load(open(src, encoding="utf-8"))
    zhs = json.load(open(zhf, encoding="utf-8"))
    by_line = {z["line"]: z["zh"] for z in zhs}
    missing = 0
    for it in items:
        zh = by_line.get(it["line"])
        if zh is None:
            missing += 1
        it["zh"] = zh
    if missing:
        print(f"!! {name}: {missing} 条缺 line 匹配")
        return False
    json.dump(items, open(done, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"合并 {len(items)} 条 -> {os.path.basename(done)}")
    return True


if __name__ == "__main__":
    cmd = sys.argv[1]
    names = sys.argv[2:]
    if not names:
        print(__doc__)
        sys.exit(1)
    ok = True
    for n in names:
        ok = (prepare(n) if cmd == "prepare" else merge(n)) and ok
    sys.exit(0 if ok else 1)
