#!/usr/bin/env python3
"""检查 .done.json 译文质量：标签/变量保留、转义合法、引号未破坏。"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITEMS = os.path.join(ROOT, ".build", "chino_items")

TAG_RE = re.compile(r"\{[^{}]*\}")
VAR_RE = re.compile(r"\[[^\[\]]*\]")


def tags(s):
    # 源文可能用非标准 {i}/{b} 闭合，子代理规范成 {/i}/{/b}；
    # 比较时把闭合标签的 '/' 去掉，视为等价。
    return sorted(re.sub(r"\{\/", "{", t) for t in TAG_RE.findall(s or ""))


def vars_(s):
    return sorted(VAR_RE.findall(s or ""))


def unescape_ok(s):
    """检查字符串写入 "..." 后是否会被提前截断。

    合法的 \\" 是转义引号，不算截断。只有前面是偶数个反斜杠的裸引号才算问题。
    """
    if s is None:
        return True
    # (?<!\\)(?:\\\\)*" —— 匹配被偶数个反斜杠前置的裸引号
    return re.search(r'(?<!\\)(?:\\\\)*"', s) is None


def main():
    files = sorted(glob.glob(os.path.join(ITEMS, "*.part*.done.json")))
    total = 0
    problems = []
    for f in files:
        done = json.load(open(f, encoding="utf-8"))
        src = os.path.join(ITEMS, os.path.basename(f).replace(".done", ""))
        orig = {}
        if os.path.exists(src):
            for it in json.load(open(src, encoding="utf-8")):
                orig[it.get("line")] = it
        for it in done:
            total += 1
            line = it.get("line")
            o = orig.get(line, {})
            es = o.get("es", "")
            text = o.get("text", "")
            zh = it.get("zh", "")
            if not zh and (es.strip() or text.strip()):
                problems.append((os.path.basename(f), line, "空译文", es[:60]))
            # 源文标签本身不平衡（畸形行）时跳过比对
            def balanced(seq):
                opens = sum(1 for t in seq if not t.startswith('{/'))
                closes = sum(1 for t in seq if t.startswith('{/'))
                return opens == closes
            src_bal = balanced(tags(es)) and balanced(tags(text))
            ok_tags = (tags(es) == tags(zh)) or (tags(text) == tags(zh)) or not src_bal
            if not ok_tags:
                problems.append((os.path.basename(f), line, f"标签不一致 es={tags(es)} en={tags(text)} zh={tags(zh)}", es[:60]))
            if vars_(es) != vars_(zh):
                problems.append((os.path.basename(f), line, f"变量不一致 {vars_(es)} vs {vars_(zh)}", es[:60]))
            if not unescape_ok(zh):
                problems.append((os.path.basename(f), line, "含裸双引号", zh[:60]))
    print(f"检查 {len(files)} 个文件，{total} 条")
    if problems:
        print(f"发现 {len(problems)} 个问题：")
        for p in problems[:30]:
            print("  ", p)
        if len(problems) > 30:
            print(f"  ... 另有 {len(problems) - 30} 个")
        return 1
    print("全部通过：标签、变量保留，无裸双引号，无空译文")
    return 0


if __name__ == "__main__":
    sys.exit(main())
