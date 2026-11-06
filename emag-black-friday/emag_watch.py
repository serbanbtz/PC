#!/usr/bin/env python3
"""Urmareste pretul unor produse eMAG si trimite notificare pe telefon (prin ntfy)
cand pretul se schimba, scade sub tinta ta sau produsul revine in stoc.

Doar biblioteca standard Python, nimic de instalat.

Exemplu:
  python emag_watch.py --topic emag-bf-serban123 ^
      "https://www.emag.ro/.../pd/DXXXXXXX/@1500" ^
      "https://www.emag.ro/.../pd/DYYYYYYY/"

  "@1500" la final = pretul maxim dorit (optional).
  --once = verifica o singura data (test) si iese.
"""
import argparse
import json
import random
import re
import secrets
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")
CAPTCHA = "captcha"


def log(msg):
    print(f"[{datetime.now():%H:%M:%S}] {msg}", flush=True)


def lei(p):
    return f"{p:,.2f}".replace(",", " ").replace(".", ",") + " lei"


def fetch(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "ro-RO,ro;q=0.9,en;q=0.8",
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")


def parse(page):
    if "eMAG Captcha" in page or "captcha-sdk.awswaf" in page:
        return CAPTCHA
    name, price, stock = None, None, None

    for block in re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', page, re.S):
        try:
            data = json.loads(block)
        except ValueError:
            continue
        items = data if isinstance(data, list) else data.get("@graph", [data]) if isinstance(data, dict) else []
        for item in items:
            if not isinstance(item, dict) or "offers" not in item:
                continue
            offers = item["offers"]
            if isinstance(offers, list):
                offers = offers[0] if offers else {}
            if isinstance(offers, dict):
                p = offers.get("price") or offers.get("lowPrice")
                if p is not None and price is None:
                    try:
                        price = float(str(p).replace(",", "."))
                    except ValueError:
                        pass
                av = offers.get("availability")
                if av and stock is None:
                    stock = str(av).rstrip("/").rsplit("/", 1)[-1]
            name = name or item.get("name")

    if price is None:  # ex: <p class="product-new-price">1.299<sup>99</sup> <span>Lei</span></p>
        m = re.search(r'class="product-new-price[^"]*"[^>]*>\s*([\d.]+)\s*<sup>(\d+)</sup>', page)
        if m:
            price = float(m.group(1).replace(".", "") + "." + m.group(2))
    if price is None:
        m = (re.search(r'itemprop="price"[^>]*content="([\d.,]+)"', page)
             or re.search(r'property="product:price:amount"[^>]*content="([\d.,]+)"', page))
        if m:
            price = float(m.group(1).replace(",", "."))
    if name is None:
        m = re.search(r'<meta property="og:title" content="([^"]+)"', page) or re.search(r'<title>([^<]+)</title>', page)
        if m:
            name = m.group(1).strip()
    return {"name": (name or "produs")[:80], "price": price, "stock": stock}


def notify(topic, title, msg, url=None, prio=3):
    body = {"topic": topic, "title": title, "message": msg, "priority": prio}
    if url:
        body["click"] = url
    req = urllib.request.Request("https://ntfy.sh/", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"}, method="POST")
    try:
        urllib.request.urlopen(req, timeout=10).read()
    except Exception as e:  # notificarea nu trebuie sa opreasca scriptul
        log(f"! notificare esuata: {e}")


def split_target(arg):
    m = re.match(r'^(https?://.+?)@(\d+(?:[.,]\d+)?)$', arg)
    return (m.group(1), float(m.group(2).replace(",", "."))) if m else (arg, None)


def main():
    ap = argparse.ArgumentParser(description="Notificari de pret eMAG pe telefon (ntfy).")
    ap.add_argument("urls", nargs="+", help="linkuri produse; optional @PRET_MAXIM la final")
    ap.add_argument("--topic", help="numele canalului ntfy (il pui si in aplicatia ntfy)")
    ap.add_argument("--interval", type=int, default=40, help="secunde intre verificari (minim 20)")
    ap.add_argument("--once", action="store_true", help="verifica o data si iese (test)")
    a = ap.parse_args()

    topic = a.topic or "emag-bf-" + secrets.token_hex(4)
    interval = max(20, a.interval)
    products = [split_target(u) for u in a.urls]
    log(f"Canal ntfy: {topic}  -> aboneaza-te la el in aplicatia ntfy de pe telefon")
    notify(topic, "eMAG watch pornit", f"Urmaresc {len(products)} produs(e), la ~{interval}s.")

    last = {}
    while True:
        blocked = False
        for url, target in products:
            status, page = fetch(url)
            info = parse(page) if status == 200 else (CAPTCHA if status in (403, 405, 429, 511) else None)
            if info == CAPTCHA:
                log(f"! eMAG a cerut captcha / a blocat (HTTP {status}). Pauza 5 minute.")
                notify(topic, "eMAG blocheaza scriptul",
                       "Captcha de la eMAG. Fac pauza 5 min. Verifica manual in aplicatie.", url, 4)
                blocked = True
                break
            if not info or info["price"] is None:
                log(f"? nu pot citi pretul (HTTP {status}): {url}")
                if url not in last:
                    notify(topic, "Nu pot citi pretul", url, url, 3)
                    last[url] = None
                continue

            p, name, stock = info["price"], info["name"], info["stock"]
            old = last.get(url)
            hit = target is not None and p <= target
            log(f"{lei(p):>14}  {stock or '':<14} {name}" + ("   <= TINTA!" if hit else ""))

            if old is None:
                msg = f"{lei(p)}" + (f" (tinta {lei(target)})" if target else "") + (f" - {stock}" if stock else "")
                notify(topic, name, msg, url, 5 if hit else 2)
            else:
                op, ostock = old
                if p != op:
                    down = p < op
                    notify(topic, ("SCADE: " if down else "Creste: ") + name,
                           f"{lei(op)} -> {lei(p)}" + ("  SUB TINTA!" if hit else ""),
                           url, 5 if (down or hit) else 3)
                if stock != ostock and stock:
                    notify(topic, f"Stoc: {name}", f"{ostock} -> {stock}", url, 5 if "InStock" in stock else 3)
            last[url] = (p, stock)
            time.sleep(1.5 + random.random() * 2)

        if a.once:
            return
        time.sleep(300 if blocked else interval + random.uniform(-5, 8))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
