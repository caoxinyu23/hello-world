#!/usr/bin/env python3
"""
把 tl/ingles 里的对话文件按 translate 块拆成小块，供并行翻译。

产物：
  .build/chino_chunks/<安全名>.rpy        待翻译块（语言名已改成 chino）
  .build/chino_chunks/<安全名>.skeleton  骨架（内容行替换成占位符，用于校验）
  .build/chino_manifest.json             清单

内容行定义：speaker "..." / "..." / old "..." / new "..."
其余行（注释、translate 头、空行）必须原样保留。
"""
import os
import re
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "game", "tl", "ingles")
OUT = os.path.join(ROOT, ".build", "chino_chunks")

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
]

TARGET_BYTES = 110 * 1024
MAX_BYTES = 230 * 1024

# 内容行：缩进 + (可选 变量名) + "..."，或 new "..."
# 注意：old "..." 是西语原文，必须原样保留，不算内容行。
CONTENT_RE = re.compile(
    r'^(?P<indent>\s*)(?P<prefix>(?:new|[A-Za-z_][A-Za-z0-9_]*)\s+)?"(?P<rest>.*)"\s*$'
)
OLD_RE = re.compile(r'^\s*old\s+".*"\s*$')


def is_content_line(line):
    s = line.rstrip("\n")
    if not s.strip():
        return False
    if OLD_RE.match(s):
        return False
    return CONTENT_RE.match(s) is not None


def split_segments(lines):
    """按 'translate ' 行切分成段；第一段是文件头部。"""
    segs = []
    cur = []
    for line in lines:
        if re.match(r"^translate ", line):
            if cur:
                segs.append(cur)
            cur = [line]
        else:
            cur.append(line)
    if cur:
        segs.append(cur)
    return segs


def skeletonize(lines):
    """把内容行的正文替换成占位符，保留缩进/前缀/引号结构。"""
    out = []
    for line in lines:
        s = line.rstrip("\n")
        if is_content_line(line):
            m = CONTENT_RE.match(s)
            indent = m.group("indent")
            prefix = m.group("prefix") or ""
            out.append(f'{indent}{prefix}"<<<CONTENT>>>"\n')
        else:
            out.append(line)
    return out


def safe_name(rel):
    return rel.replace("/", "__")


def main():
    os.makedirs(OUT, exist_ok=True)
    manifest = []
    for rel in DIALOGUE_FILES:
        path = os.path.join(SRC, rel)
        if not os.path.exists(path):
            print(f"!! 缺失 {rel}")
            continue
        with open(path, encoding="utf-8", errors="ignore") as fh:
            lines = fh.readlines()

        segs = split_segments(lines)
        # 合并头部到第一段
        if segs and not re.match(r"^translate ", segs[0][0]):
            pass

        # 按体积聚合段
        chunks = []
        cur = []
        cur_bytes = 0
        for seg in segs:
            sb = sum(len(x.encode("utf-8")) for x in seg)
            if cur and cur_bytes + sb > TARGET_BYTES:
                chunks.append(cur)
                cur = []
                cur_bytes = 0
            cur.extend(seg)
            cur_bytes += sb
        if cur:
            chunks.append(cur)

        base = safe_name(rel)
        for i, ch in enumerate(chunks):
            # 语言名 ingles -> chino
            out_lines = []
            for ln in ch:
                if ln.startswith("translate ingles "):
                    ln = ln.replace("translate ingles ", "translate chino ", 1)
                out_lines.append(ln)
            name = f"{base}.part{i:02d}"
            with open(os.path.join(OUT, name + ".rpy"), "w", encoding="utf-8") as fh:
                fh.writelines(out_lines)
            with open(os.path.join(OUT, name + ".skeleton"), "w", encoding="utf-8") as fh:
                fh.writelines(skeletonize(out_lines))
            ncontent = sum(1 for x in out_lines if is_content_line(x))
            manifest.append({
                "file": rel,
                "part": i,
                "name": name,
                "chunks": len(chunks),
                "bytes": sum(len(x.encode("utf-8")) for x in out_lines),
                "lines": len(out_lines),
                "content_lines": ncontent,
            })
            print(f"{name:45s} {len(out_lines):6d} 行  {ncontent:5d} 内容行  {manifest[-1]['bytes']//1024:4d} KB")

    with open(os.path.join(ROOT, ".build", "chino_manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, ensure_ascii=False, indent=1)
    print(f"\n共 {len(manifest)} 块，总内容行 {sum(m['content_lines'] for m in manifest)}")


if __name__ == "__main__":
    main()
