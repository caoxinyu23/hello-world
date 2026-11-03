#!/usr/bin/env python3
"""
chino_pipeline.py —— ToEataGod 汉化条目抽取 / 组装 / 校验

子命令：
  prepare   从 game/tl/ingles 抽取待译条目 -> .build/chino_items/<safe>.json
            并按 400 条切分 -> .build/chino_items/<safe>.partN.json
  assemble  读取译文 -> 生成 game/tl/chino/<file>.rpy
  verify    校验生成的中文文件结构

设计要点：
  - 只替换「内容行」的引号内文本；缩进、说话人变量、old 行、注释、translate 头
    全部原样保留。
  - 内容行：speaker "..." / "..." / new "..."
  - old "..." 是西语原文，永不改动。
"""
import os
import re
import json
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "game", "tl", "ingles")
OUT_TL = os.path.join(ROOT, "game", "tl", "chino")
ITEMS = os.path.join(ROOT, ".build", "chino_items")

DIALOGUE_FILES = [
    "script.rpy",
    "rutas/labelsact2.rpy",
    "rutas/memorias.rpy",
    "rutas/minirutas.rpy",
    "rutas/nulla.rpy",
    "rutas/pantallas.rpy",
    "rutas/rafael.rpy",
    "rutas/septem.rpy",
    "rutas/unum.rpy",
    "common.rpy",
]

# 内容行：缩进 + (可选 变量名) + "..." + 可选尾注释
CONTENT_RE = re.compile(
    r'^(?P<indent>\s*)(?P<prefix>(?:new|[A-Za-z_][A-Za-z0-9_]*)\s+)?"(?P<text>.*)"(?P<trailer>\s*#.*)?$'
)
OLD_RE = re.compile(r'^\s*old\s+"(?P<text>.*)"\s*$')
# 可能跨行的字符串起点
START_RE = re.compile(r'^(?P<indent>\s*)(?P<prefix>(?:new|[A-Za-z_][A-Za-z0-9_]*)\s+)?"')
COMMENT_RE = re.compile(r'^\s*#')

PART_SIZE = 400


def safe_name(rel):
    return rel.replace("/", "__")


def extract_quote(s):
    ms = re.findall(r'"((?:[^"\\]|\\.)*)"', s)
    return ms[-1] if ms else ""


def iter_content(lines):
    """
    遍历文件行，产出 (start, end, item)。
    item: {indent, prefix, trailer, text, es}
    """
    n = len(lines)
    i = 0
    last_es = ""
    while i < n:
        raw = lines[i]
        s = raw.rstrip("\n")

        # 注释行：记录西语源文
        if COMMENT_RE.match(s):
            last_es = extract_quote(s)
            i += 1
            continue

        # old 行：记录西语源文，本身不译
        mold = OLD_RE.match(s)
        if mold:
            last_es = mold.group("text")
            i += 1
            continue

        m = CONTENT_RE.match(s)
        if m:
            yield (i, i + 1, {
                "indent": m.group("indent"),
                "prefix": m.group("prefix") or "",
                "trailer": m.group("trailer") or "",
                "text": m.group("text"),
                "es": last_es,
            })
            last_es = ""
            i += 1
            continue

        # 跨行字符串：本行有起始引号但未闭合
        mstart = START_RE.match(s)
        if mstart and s.rstrip() and not s.rstrip().endswith('"'):
            j = i
            buf = s
            while j < n and not buf.rstrip().endswith('"'):
                j += 1
                if j < n:
                    buf += "\n" + lines[j].rstrip("\n")
            # 解析拼接后的整串
            m2 = CONTENT_RE.match(buf)
            if m2:
                yield (i, j + 1, {
                    "indent": m2.group("indent"),
                    "prefix": m2.group("prefix") or "",
                    "trailer": m2.group("trailer") or "",
                    "text": m2.group("text"),
                    "es": last_es,
                    "multiline": True,
                })
                last_es = ""
                i = j + 1
                continue
        i += 1


def load_lines(rel):
    with open(os.path.join(SRC, rel), encoding="utf-8", errors="ignore") as fh:
        return fh.readlines()


def cmd_prepare():
    os.makedirs(ITEMS, exist_ok=True)
    manifest = []
    for rel in DIALOGUE_FILES:
        lines = load_lines(rel)
        items = []
        for (a, b, it) in iter_content(lines):
            it["line"] = a + 1
            it["end_line"] = b
            items.append(it)
        safe = safe_name(rel)
        with open(os.path.join(ITEMS, safe + ".json"), "w", encoding="utf-8") as fh:
            json.dump(items, fh, ensure_ascii=False, indent=1)
        # 分块
        parts = [items[i:i + PART_SIZE] for i in range(0, len(items), PART_SIZE)]
        for pi, part in enumerate(parts):
            with open(os.path.join(ITEMS, f"{safe}.part{pi:02d}.json"), "w", encoding="utf-8") as fh:
                json.dump(part, fh, ensure_ascii=False, indent=1)
        manifest.append({"file": rel, "safe": safe, "items": len(items), "parts": len(parts)})
        print(f"{rel:35s} {len(items):5d} 条 -> {len(parts)} 块")
    with open(os.path.join(ROOT, ".build", "chino_items_manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=1)
    print(f"\n总计 {sum(m['items'] for m in manifest)} 条")


def cmd_assemble():
    os.makedirs(OUT_TL, exist_ok=True)
    os.makedirs(os.path.join(OUT_TL, "rutas"), exist_ok=True)
    total = 0
    for rel in DIALOGUE_FILES:
        safe = safe_name(rel)
        items_path = os.path.join(ITEMS, safe + ".json")
        if not os.path.exists(items_path):
            print(f"!! 缺少条目文件 {safe}.json")
            continue
        with open(items_path, encoding="utf-8") as fh:
            items = json.load(fh)

        # 收集译文：优先 .done.json（子代理产物），否则 part 文件
        trans = {}
        base = os.path.join(ITEMS, safe)
        idx = 0
        for pi in range(200):
            p = f"{base}.part{pi:02d}.json"
            dp = f"{base}.part{pi:02d}.done.json"
            if not os.path.exists(p) and not os.path.exists(dp):
                break
            src = dp if os.path.exists(dp) else p
            with open(src, encoding="utf-8") as fh:
                for it in json.load(fh):
                    if it.get("zh"):
                        trans[idx] = it["zh"]
                    idx += 1
        # 兜底：整文件里的 zh
        if not trans:
            for i, it in enumerate(items):
                if it.get("zh"):
                    trans[i] = it["zh"]

        lines = load_lines(rel)
        out = assemble_file(lines, items, trans)
        dest = os.path.join(OUT_TL, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as fh:
            fh.writelines(out)
        missing = len(items) - len(trans)
        total += len(out)
        print(f"{rel:35s} 写出 {len(out)} 行，缺失译文 {missing} 条")
    print(f"\n完成，共 {total} 行")


def assemble_file(lines, items, trans):
    """稳妥版：按 iter_content 的顺序逐段重建。

    注意：源文件的 `translate ingles <id>:` 头必须改写为 `translate chino <id>:`，
    否则中文文件不会被 Ren'Py 识别。
    """
    out = []
    ii = 0
    pos = 0
    for (a, b, it) in iter_content(lines):
        out.extend(lines[pos:a])
        pos = b
        zh = trans.get(ii)
        ii += 1
        trailer = it.get("trailer", "") or ""
        if zh is None:
            out.append(lines[a])
        else:
            out.append(f'{it["indent"]}{it["prefix"]}"{zh}"{trailer}\n')
    out.extend(lines[pos:])
    # 重写 translate 语言头（整文件级）
    out = [
        re.sub(r"^translate ingles\b", "translate chino", l)
        if l.startswith("translate ingles") else l
        for l in out
    ]
    return out


def cmd_verify():
    ok = True
    for rel in DIALOGUE_FILES:
        src = os.path.join(SRC, rel)
        dst = os.path.join(OUT_TL, rel)
        if not os.path.exists(dst):
            print(f"!! 缺少 {rel}")
            ok = False
            continue
        sl = open(src, encoding="utf-8", errors="ignore").read().split("\n")
        dl = open(dst, encoding="utf-8", errors="ignore").read().split("\n")
        # translate 头：源是 ingles，输出必须是 chino，且标识符保持一致
        def headers(ls):
            return [l for l in ls if l.startswith("translate ")]
        hs, hd = headers(sl), headers(dl)
        def norm(h):
            return re.sub(r"^translate \S+", "translate X", h)
        if [norm(h) for h in hs] != [norm(h) for h in hd]:
            print(f"!! {rel}: translate 头数量/标识符不一致 ({len(hs)} vs {len(hd)})")
            ok = False
        else:
            # 输出头必须全部是 chino
            bad = [h for h in hd if not h.startswith("translate chino")]
            if bad:
                print(f"!! {rel}: 存在非 chino 的 translate 头 {len(bad)} 个，如 {bad[0]!r}")
                ok = False
            else:
                print(f"OK {rel}: {len(hd)} 个 translate chino 头一致")
        # old 行必须一致
        def olds(ls):
            return [l for l in ls if l.lstrip().startswith("old ")]
        if olds(sl) != olds(dl):
            print(f"  !! {rel}: old 行不一致")
            ok = False
    return ok


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "prepare"
    if cmd == "prepare":
        cmd_prepare()
    elif cmd == "assemble":
        cmd_assemble()
    elif cmd == "verify":
        sys.exit(0 if cmd_verify() else 1)
    else:
        print(__doc__)
