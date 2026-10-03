# Campania „Fără povești. Doar acte.” · West Auto Botoșani

Campania de toamnă pentru Facebook și TikTok, construită de la zero pe baza a tot ce s-a lucrat până acum (postările programate, planul pe octombrie, schema de filmare).

**Pe scurt:** oamenii nu se tem de prețul unei mașini second-hand, se tem de țeapă. West Auto are deja dovezile (carte service, rapoarte, facturi), dar le arată ca pe niște bife. Campania le face mesajul principal: fiecare mașină din parc are un **dosar**, iar oricine îl poate cere scriind **DOSAR** pe WhatsApp.

| | |
|---|---|
| **Perioada** | Pregătire 4–6 oct · Lansare 7 oct · Final 1 nov · Raport 2 nov |
| **Obiectiv** | Conversații WhatsApp despre o mașină anume → test drive → vânzare |
| **Buget recomandat** | ≈ 1.380 lei (Meta ≈ 1.110 lei, TikTok Promote ≈ 270 lei) |
| **Ținta principală** | Cost pe conversație ≤ 20 lei, cel puțin 70 de conversații DOSAR |
| **Timpul tău** | ≈ 2 ore de pregătire până marți, apoi 15 min lunea și o filmare pe săptămână |

## Documentele, în ordinea de lucru

1. [`01-audit.md`](01-audit.md): ce s-a făcut, ce e programat, ce lipsește (inclusiv riscurile legale de verificat)
2. [`02-strategie.md`](02-strategie.md): obiective, public, ideea, canale, buget, faze, riscuri
3. [`03-texte.md`](03-texte.md): toate textele gata de copiat (reclame, postări, TikTok, WhatsApp, răspunsuri la comentarii)
4. [`04-scripturi-video.md`](04-scripturi-video.md): cele 5 tipuri de clipuri, cadru cu cadru
5. [`05-calendar.md`](05-calendar.md): fiecare zi, 4 octombrie – 2 noiembrie
6. [`06-lansare.md`](06-lansare.md): pașii exacți până la publicare, verificarea dinainte și rutina de luni
7. [`vizuale/`](vizuale): 31 de imagini gata de încărcat

## Vizualele

| Fișier | Format | Unde se folosește |
|---|---|---|
| `01-manifest-feed.png` | 1080×1350 | Postarea de lansare, reclama A1 |
| `02-manifest-story.png` | 1080×1920 | Stories, Reels, postarea foto TikTok |
| `03-carusel-1…6.png` | 1080×1350 | Caruselul „Ce e în dosar”, reclama A2 |
| `04-stoc-feed.png` | 1080×1350 | Stocul cu dosar, reclama A3 |
| `05-dosar-[mașina].png` | 1080×1350 | Dosarul fiecăreia dintre cele 19 mașini: reclamele din setul B, „Dosarul săptămânii” și imaginea trimisă pe WhatsApp |
| `06-video-final.png` | 1080×1920 | Cadrul final al fiecărui clip |
| `07-video-eticheta.png` | 1080×1920, transparent | Eticheta „Fără povești” pusă peste clipuri |
| `08-coperta-facebook.png` | 1640×624 | Coperta paginii |

Fotografiile mașinilor sunt decupate din posterele existente. Prețurile și datele vin din postările programate pe 29 septembrie: **verifică stocul și prețurile înainte de publicare.**

## Ce am nevoie de la tine ca să pornim

1. OK pe concept și pe cuvântul DOSAR
2. Bugetul (Minim / Recomandat / Accelerat)
3. Cine apare în clipuri
4. Ce mașini s-au vândut din 29 septembrie
5. Verificarea identității de advertiser în Ads Manager (doar tu o poți face)
6. Cine răspunde pe WhatsApp joi, 8 octombrie

## Pentru modificări

`sursa/` conține tot ce a generat materialele. Vizualele se refac cu `npm install` (fonturile Montserrat și Source Sans 3), `python3 gen.py` și `node render.js`. Textele, calendarul și pașii se schimbă în `sursa/date_campanie.py`, apoi `python3 date_campanie.py` rescrie `campanie.json` și documentele 03–06.
