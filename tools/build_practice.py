#!/usr/bin/env python3
"""Build the interview practice page from the two interview guides.

Usage: python3 tools/build_practice.py
Reads tesla-interview/Pregatire_Interviu_Tesla_Iasi*.md and Plan_30_60_90_Iasi.md,
writes tesla-interview/Antrenament_Interviu.html.
"""
import json
import pathlib
import re

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIR = ROOT / "tesla-interview"
TEMPLATE = pathlib.Path(__file__).parent / "practice_template.html"


def md(text):
    html = markdown.markdown(text, extensions=["tables", "sane_lists"])
    return re.sub(r"(\[[^\]<>]{1,80}\])(?!\()", r'<mark class="fill">\1</mark>', html)


def cards(path):
    s = path.read_text(encoding="utf-8")
    s = s[s.index("\n## 4."):s.index("\n## 6.")]
    out = []
    for blk in re.split(r"^### ", s, flags=re.M)[1:]:
        head, body = blk.split("\n", 1)
        m = re.match(r"([0-9]+|[A-H])\.\s*(.*)", head.strip())
        cid, title = m.group(1), m.group(2).strip()
        body = body.split("\n---")[0].split("\n## ")[0]
        parts = re.split(r"^(?=\*\*(?:Follow-up|Și dacă insistă|And if they push))", body, flags=re.M)
        main = parts[0].strip()
        asked = None
        first_line = re.match(r"\*([^*\n]+)\*\n", main + "\n")
        if first_line and not main.startswith("*("):
            asked = first_line.group(1).strip()
            main = main[first_line.end():].strip()
        group = "guide" if cid.isdigit() else "new"
        out.append(dict(id=cid, title=title, asked=asked, body=main, group=group))
        for i, p in enumerate(parts[1:]):
            first, rest = (p.split("\n", 1) + [""])[:2]
            q = re.search(r"„(.+?)”", first)
            rest, asked_f = rest.strip(), None
            m_f = re.match(r"\*([^*\n]+)\*\n", rest + "\n")
            if m_f:
                asked_f, rest = m_f.group(1).strip(), rest[m_f.end():].strip()
            note = first.split("**", 2)[-1].strip() if first.count("**") >= 2 else ""
            if note:
                rest = note + "\n\n" + rest
            out.append(dict(id=f"{cid}.{i + 1}", title=q.group(1) if q else first.strip("*"),
                            asked=asked_f, body=rest, group="followup"))
    return out


def clean_q(text):
    text = re.sub(r"^Situa\w+:\s*", "", text)
    text = text.strip().strip("„”\"")
    return re.sub(r"\s*\(.*?\)$", "", text) if "pâlnia" in text else text


COMPETITORS_EN = """> Tesla led the Romanian EV market in the first half: Model Y was number one, with around 800 units. But in August, MG and BYD caught up. MG4 was the top EV that month and BYD was the top brand. Then there's the VW group, Hyundai and Kia, Dacia Spring, and imported used EVs, a market I know from the inside.
>
> The Chinese brands compete on price. Tesla wins on what a local store controls: **test drives, service close to home in Brătuleni, and the delivery experience**, plus the Supercharger network and over-the-air updates.

*Cifrele vin din fișa Fapte_Tesla_Romania_Oct2026. Spune-le aproximativ, nu le recita.*"""

COMPETITORS_RO = """> Tesla a condus piața de electrice din România în prima jumătate a anului: Model Y a fost pe primul loc, cu aproximativ 800 de unități. Dar în august, MG și BYD au recuperat: MG4 a fost cea mai înmatriculată electrică a lunii, iar BYD marca nr. 1. Mai sunt grupul VW, Hyundai și Kia, Dacia Spring și importurile de electrice second-hand, o piață pe care o cunosc din interior.
>
> Mărcile chinezești concurează pe preț. Tesla câștigă la ce controlează un magazin local: **test drive-uri, service aproape de casă, în Brătuleni, și experiența de livrare**, plus rețeaua de Supercharger-e și actualizările OTA.

*Cifrele vin din fișa Fapte_Tesla_Romania_Oct2026. Spune-le aproximativ, nu le recita.*"""


def main():
    en = cards(DIR / "Pregatire_Interviu_Tesla_Iasi.md")
    ro = cards(DIR / "Pregatire_Interviu_Tesla_Iasi_RO.md")
    assert [c["id"] for c in en] == [c["id"] for c in ro], "guides are out of sync"

    plan = (DIR / "Plan_30_60_90_Iasi.md").read_text(encoding="utf-8")
    spoken = plan[plan.index("## The 60-second spoken version"):plan.index("## Pe scurt")]
    spoken = "\n".join(spoken.split("\n")[2:]).strip()
    rezumat = plan[plan.index("## Pe scurt în română"):].split("\n", 1)[1].strip()

    data = []
    for e, r in zip(en, ro):
        q_en = r["asked"] or clean_q(e["title"])
        en_body, ro_body = e["body"], r["body"]
        if e["id"] == "H":
            en_body = COMPETITORS_EN + "\n\n" + en_body
            ro_body = COMPETITORS_RO + "\n\n" + ro_body
        if e["id"] == "E":
            en_body = spoken + "\n\n*Versiunea din planul pe 30-60-90 de zile.*"
            ro_body = rezumat
        data.append(dict(
            id=e["id"], group=e["group"],
            q_en=q_en, q_ro=clean_q(r["title"]),
            a_en=md(en_body), a_ro=md(ro_body),
        ))

    page = TEMPLATE.read_text(encoding="utf-8").replace(
        "__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    out = DIR / "Antrenament_Interviu.html"
    out.write_text(page, encoding="utf-8")
    print(f"{len(data)} cards -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
