# eMAG Black Friday – notificări de preț pe telefon

Scriptul verifică paginile produselor tale la ~40 de secunde. Îți trimite notificare pe telefon când prețul se schimbă, când scade sub ținta ta sau când produsul revine în stoc. Dacă atingi notificarea, se deschide produsul.

**Nu cumpără nimic singur.** Comanda o plasezi tu, în aplicație.

## Pornire în 3 pași

1. **Pe telefon:** instalează aplicația **ntfy** (Play Store / App Store). Apasă `+` și abonează-te la un nume unic, de exemplu `emag-bf-serban123`.
2. **Pe PC:** ai nevoie de Python 3. Pe Windows îl iei din Microsoft Store („Python 3.12”). Descarcă `emag_watch.py`.
3. **Rulează** în terminal, în folderul cu scriptul:

```
python emag_watch.py --topic emag-bf-serban123 "LINK_PRODUS_1@1500" "LINK_PRODUS_2"
```

- `@1500` la finalul linkului înseamnă prețul maxim dorit. E opțional; când prețul ajunge sub el, primești notificare urgentă.
- Mai întâi testează cu `--once`. Trebuie să vezi prețul în terminal și să primești notificarea pe telefon.

## Important
- Rulează pe PC-ul de acasă: eMAG blochează serverele din cloud cu captcha.
- Nu coborî intervalul mult sub 40 s. Dacă eMAG vede trafic neobișnuit din rețeaua ta, poate cere captcha pe tot Wi-Fi-ul. Atunci telefonul tău ar primi captcha fix la start. Ca să fii sigur, ține telefonul pe **date mobile** în primele minute.
- Dacă primești notificarea „eMAG blochează scriptul”, scriptul face singur pauză 5 minute. Tu continuă manual în aplicație.
