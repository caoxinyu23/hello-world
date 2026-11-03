#!/usr/bin/env python3
"""把分块翻译的子块 .done.json 合并回完整 part 的 .done.json。

背景：大 part（>200 条）拆成 100 条子块分别翻译。本脚本按文件名顺序
把 <base>.partNN.s*.done.json 合并成 <base>.partNN.done.json，
并校验合并后的条目数与原始 part 一致。
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITEMS = os.path.join(ROOT, ".build", "chino_items")


def part_key(path):
    """排序键：按数字段排序，保证 s00 < s01 < ... < s00.s00 等。"""
    return [int(x) if x.isdigit() else x for x in re.split(r"[.\-]", path)]


def merge_part(base):
    """base 形如 <safe>.partNN（不含 .json）。"""
    full = os.path.join(ITEMS, base + ".done.json")
    if os.path.exists(full):
        print(f"跳过（已有完整 done）: {base}")
        return True
    # 找子块 done 文件
    subs = sorted(glob.glob(os.path.join(ITEMS, f"{base}.s*.done.json")), key=part_key)
    if not subs:
        return True
    merged = []
    for sp in subs:
        merged.extend(json.load(open(sp, encoding="utf-8")))
    # 校验与原始 part 条目数一致
    src = os.path.join(ITEMS, base + ".json")
    if os.path.exists(src):
        n_src = len(json.load(open(src, encoding="utf-8")))
        if n_src != len(merged):
            print(f"!! {base}: 合并 {len(merged)} 条，但原 part {n_src} 条，不匹配")
            return False
    json.dump(merged, open(full, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"合并 {len(merged)} 条 ({len(subs)} 个子块) -> {os.path.basename(full)}")
    return True


def main():
    ok = True
    for f in sorted(glob.glob(os.path.join(ITEMS, "*.part*.json"))):
        b = os.path.basename(f)[:-len(".json")]
        if b.endswith(".done") or b.endswith(".src") or b.endswith(".zh"):
            continue
        if not re.search(r"\.part\d+$", b):
            continue
        ok = merge_part(b) and ok
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
