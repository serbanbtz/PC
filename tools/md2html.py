#!/usr/bin/env python3
"""Convert a Markdown guide to a phone-friendly HTML page in the same style as the interview guide.

Usage: python3 tools/md2html.py input.md [output.html]
"""
import pathlib
import re
import sys
import unicodedata

import markdown

HERE = pathlib.Path(__file__).parent
CSS = (HERE / "style.css.html").read_text(encoding="utf-8")


def slug(text):
    text = unicodedata.normalize("NFKD", re.sub(r"<[^>]+>", "", text))
    text = "".join(c for c in text if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def convert(src, dst):
    md_text = src.read_text(encoding="utf-8")
    html = markdown.markdown(md_text, extensions=["tables", "sane_lists"])
    html = re.sub(r"<li>(?:\[ \] |☐ )", '<li class="todo">☐ ', html)
    html = re.sub(r"(\[[^\]<>]{1,80}\])(?!\()", r'<mark class="fill">\1</mark>', html)
    html = re.sub(r"<table>", '<div class="tbl"><table>', html)
    html = re.sub(r"</table>", "</table></div>", html)

    toc = []

    def add_id(m):
        level, inner = m.group(1), m.group(2)
        anchor = slug(inner)
        if level == "2":
            toc.append(f'<a href="#{anchor}">{re.sub(r"<[^>]+>", "", inner)}</a>')
        return f'<h{level} id="{anchor}">{inner}</h{level}>'

    html = re.sub(r"<h([1-3])>(.*?)</h\1>", add_id, html)
    title_match = re.search(r"^# (.+)$", md_text, re.M)
    title = title_match.group(1).split("·")[0].split("–")[0].strip() if title_match else src.stem
    nav = f'<nav class="toc">{"".join(toc)}</nav>\n' if toc else ""
    page = (
        '<!doctype html>\n<html lang="ro"><head><meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{title}</title>\n{CSS}</head>\n<body>\n{nav}<main>\n{html}\n</main>\n</body></html>\n"
    )
    dst.write_text(page, encoding="utf-8")


if __name__ == "__main__":
    src = pathlib.Path(sys.argv[1])
    dst = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".html")
    convert(src, dst)
    print(f"{src} -> {dst}")
