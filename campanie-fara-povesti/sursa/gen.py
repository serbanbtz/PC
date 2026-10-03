# Generează HTML-urile pentru vizualele campaniei „Fără povești” (West Auto Botoșani).
# Fiecare fișier din html/ se randează apoi la dimensiunea din MANIFEST cu render.js.
import json, os, html

os.makedirs('html', exist_ok=True)
cars = {c['key']: c for c in json.load(open('cars.json'))}

SHORT = {
    'duster': 'Dacia Duster', 'tiguan': 'VW Tiguan 4Motion', 'teslay': 'Tesla Model Y Performance',
    'clio': 'Renault Clio', 'qqt': 'Nissan Qashqai automat', 'chr': 'Toyota C-HR Hybrid',
    'p207': 'Peugeot 207 SW', 'sportA': 'Kia Sportage 4x4 automat', 'tesla3': 'Tesla Model 3 Long Range',
    'golf': 'VW Golf 5', 'arona': 'SEAT Arona', 'qq2': 'Nissan Qashqai+2, 7 locuri',
    'laguna': 'Renault Laguna', 'scenic': 'Renault Scenic', 'a6man': 'Audi A6 S-Line',
    'kangoo': 'Renault Kangoo', 'v40': 'Volvo V40', 'sportM': 'Kia Sportage 4x4 manual', 'toledo': 'SEAT Toledo',
}
for k, c in cars.items():
    c['short'] = SHORT[k]
json.dump(list(cars.values()), open('cars.json', 'w'), ensure_ascii=False, indent=1)

E = html.escape
WA = '0771 311 941'
ADDR = 'Bd. Mihai Eminescu 2A, Botoșani'

HEAD = '''<!doctype html><html lang="ro"><head><meta charset="utf-8">
<link rel="stylesheet" href="../node_modules/@fontsource/montserrat/700.css">
<link rel="stylesheet" href="../node_modules/@fontsource/montserrat/800.css">
<link rel="stylesheet" href="../node_modules/@fontsource/montserrat/900.css">
<link rel="stylesheet" href="../node_modules/@fontsource/source-sans-3/400.css">
<link rel="stylesheet" href="../node_modules/@fontsource/source-sans-3/600.css">
<link rel="stylesheet" href="../node_modules/@fontsource/source-sans-3/700.css">
<style>
/* Identitatea West Auto din posterele existente: antracit, auriu, Montserrat foarte bold. */
:root{
  --bg-1:#0e1013; --bg-2:#1d2025; --ink:#f4f2ec; --muted:#a6a9ae; --line:rgba(255,255,255,.13);
  --gold:#d9ae55; --gold-2:#b8893a; --gold-ink:#241a06; --strike:#e0533f;
  --paper:#f3efe6; --paper-ink:#1b1d21; --paper-muted:#5d6067; --paper-line:#ddd6c7;
  --display:"Montserrat","Arial Black",sans-serif; --body:"Source Sans 3","Segoe UI",Arial,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:100%;height:100%}
body{font-family:var(--body);color:var(--ink);
  background:radial-gradient(120% 80% at 80% 0%,#2a2e34 0%,var(--bg-2) 35%,var(--bg-1) 100%);
  -webkit-font-smoothing:antialiased;overflow:hidden}
body.clear{background:transparent}
.frame{position:absolute;inset:0;display:flex;flex-direction:column}
.brand{font:700 22px/1 var(--display);letter-spacing:.26em;color:var(--gold);text-transform:uppercase;display:flex;align-items:center;gap:18px}
.brand::after{content:"";flex:1;height:2px;background:linear-gradient(90deg,var(--gold),transparent)}
.eyebrow{font:800 22px/1 var(--display);letter-spacing:.2em;color:var(--gold);text-transform:uppercase}
.h-xl{font:900 118px/1.06 var(--display);letter-spacing:-.01em;text-transform:uppercase}
.h-l{font:900 84px/1.08 var(--display);letter-spacing:-.01em;text-transform:uppercase}
.h-m{font:900 62px/1.04 var(--display);text-transform:uppercase}
.gold{color:var(--gold)}
.muted{color:var(--muted)}
.quote{font:600 46px/1.15 var(--body);color:var(--muted);text-decoration:line-through;text-decoration-color:var(--strike);text-decoration-thickness:5px}
.checks{list-style:none;display:flex;flex-direction:column;gap:18px}
.checks li{display:flex;gap:20px;align-items:flex-start;font:600 34px/1.2 var(--body)}
.checks li::before{content:"";flex:none;width:36px;height:36px;margin-top:2px;border-radius:50%;
  background:var(--gold) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='%23241a06' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/24px no-repeat}
.cta{display:flex;align-items:center;justify-content:space-between;gap:24px;border-radius:18px;padding:28px 36px;
  background:linear-gradient(135deg,#e8c574 0%,var(--gold) 45%,var(--gold-2) 100%);color:var(--gold-ink)}
.cta b{font:900 40px/1.05 var(--display);text-transform:uppercase}
.cta span{font:800 38px/1 var(--display);white-space:nowrap;font-variant-numeric:tabular-nums}
.foot{display:flex;justify-content:space-between;font:600 24px/1 var(--body);color:var(--muted);border-top:1px solid var(--line);padding-top:24px}
.foot b{color:var(--ink);font-weight:700}
.dots{display:flex;gap:10px}.dots i{width:12px;height:12px;border-radius:50%;background:var(--line)}.dots i.on{background:var(--gold)}
.example{border:2px solid var(--line);border-radius:18px;padding:30px 34px;display:flex;flex-direction:column;gap:12px;background:rgba(255,255,255,.03)}
.example small{font:800 20px/1 var(--display);letter-spacing:.18em;color:var(--gold);text-transform:uppercase}
.example p{font:600 37px/1.3 var(--body)}
.body-l{font:400 44px/1.35 var(--body);color:#dcdad4}
.num{font:900 220px/.8 var(--display);color:transparent;-webkit-text-stroke:3px var(--gold)}
.fitbox>span{display:block;white-space:nowrap}
</style>
<script>
// Micșorează titlurile .fitbox până când fiecare rând încape pe lățime.
document.fonts.ready.then(()=>{document.querySelectorAll('.fitbox').forEach(h=>{
  let fs=parseFloat(getComputedStyle(h).fontSize);
  const ok=()=>[...h.children].every(c=>c.scrollWidth<=h.clientWidth+1);
  while(!ok()&&fs>20){fs-=2;h.style.fontSize=fs+'px';}
  document.body.dataset.fit='1';});});
</script></head>'''

CHECK_SVG_DARK = ''


def page(name, body, cls=''):
    with open(f'html/{name}.html', 'w') as f:
        f.write(HEAD + f'<body class="{cls}">' + body + '</body></html>')


MANIFEST = []  # (fișier, lățime, înălțime, transparent)

QUOTES = ['„A fost a unui neamț bătrân.”', '„A plâns când a vândut-o.”', '„Km reali, pe cuvânt.”']
DOSAR_ITEMS = ['Istoric de service și facturi', 'Raport de istoric pe seria de șasiu',
               'Kilometri pe care îi poți verifica', 'Test drive înainte de orice decizie',
               'Garanție 12 luni, în scris']


def manifest(name, w, h, pad_top, pad_bottom, qsize, hsize):
    qs = ''.join(f'<p class="quote" style="font-size:{qsize}px">{E(q)}</p>' for q in QUOTES)
    items = ''.join(f'<li>{E(i)}</li>' for i in DOSAR_ITEMS)
    page(name, f'''<div class="frame" style="padding:{pad_top}px 72px {pad_bottom}px;gap:0">
  <div class="brand">West Auto Botoșani</div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:44px">
    <div style="display:flex;flex-direction:column;gap:14px">
      <p class="eyebrow" style="color:var(--muted);letter-spacing:.16em">Ce auzi de obicei la mașini second-hand</p>{qs}
    </div>
    <h1 class="h-xl fitbox" style="font-size:{hsize}px"><span>Fără povești.</span><span class="gold">Doar acte.</span></h1>
    <div style="display:flex;flex-direction:column;gap:22px">
      <p style="font:700 34px/1.2 var(--body)">Fiecare mașină din parc are un dosar pe care îl vezi înainte să plătești:</p>
      <ul class="checks">{items}</ul>
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:26px">
    <div class="cta"><b>Scrie DOSAR<br>pe WhatsApp</b><span>{WA}</span></div>
    <div class="foot"><span>{ADDR}</span><span>lângă Kaufland Gară</span></div>
  </div>
</div>''')
    MANIFEST.append((name, w, h, False))


manifest('01-manifest-feed', 1080, 1350, 64, 56, 44, 116)
# Story/Reels/TikTok: zona de sus (~220 px) și cea de jos (~380 px) rămân libere pentru interfața aplicației.
manifest('02-manifest-story', 1080, 1920, 230, 400, 46, 130)

# Carusel „Ce e în dosar” (6 cadre, 1080x1350)
CARDS = [
    None,
    ('01', 'Istoricul de service', 'Carte service, facturi, ce s-a schimbat și când. Lista exactă, nu „i-am făcut de toate”.',
     'Volvo V40 · 2014', 'Distribuție, kit ambreiaj cu volantă, brațe de suspensie, discuri și plăcuțe: toate noi în 04.2026.'),
    ('02', 'Raportul de istoric', 'Raport pe seria de șasiu: kilometrii înregistrați de-a lungul anilor, daunele declarate, țările prin care a trecut.',
     'Kia Sportage 4x4 automat · 2014', 'Raport CarVertical, carte service în reprezentanță, ITP efectuat la 259.000 km.'),
    ('03', 'Kilometri verificabili', 'Compari singur kilometrajul din bord cu cartea de service și cu raportul. Durează două minute.',
     'Dacia Duster · 2013', '139.000 km la bord. Cartea de service e completată până la 130.000 km.'),
    ('04', 'Garanție 12 luni, în scris', 'Scrisă în contract, cu ce acoperă. Și test drive înainte de orice decizie.',
     'Renault Clio · 2018', '12 luni garanție fără limită de km, carte service completă în reprezentanță.'),
    None,
]
TOTAL = 6


def dots(i):
    return '<div class="dots">' + ''.join(f'<i class="{"on" if k == i else ""}"></i>' for k in range(TOTAL)) + '</div>'


folder = '''<div style="position:relative;width:520px;height:380px;align-self:flex-end;margin-right:-8px">
  <div style="position:absolute;left:0;top:0;width:210px;height:62px;border-radius:18px 18px 0 0;background:var(--gold-2)"></div>
  <div style="position:absolute;left:0;top:44px;right:0;bottom:0;border-radius:0 22px 22px 22px;background:linear-gradient(160deg,#e3bd69,var(--gold-2));box-shadow:0 30px 60px rgba(0,0,0,.45)"></div>
  <div style="position:absolute;left:46px;right:46px;top:8px;height:250px;border-radius:10px;background:var(--paper);transform:rotate(-3deg);box-shadow:0 8px 20px rgba(0,0,0,.25);padding:30px 34px;display:flex;flex-direction:column;gap:16px">
    <i style="display:block;height:14px;width:60%;background:var(--paper-line);border-radius:7px"></i>
    <i style="display:block;height:14px;width:85%;background:var(--paper-line);border-radius:7px"></i>
    <i style="display:block;height:14px;width:72%;background:var(--paper-line);border-radius:7px"></i>
    <i style="display:block;height:14px;width:80%;background:var(--paper-line);border-radius:7px"></i>
  </div>
  <div style="position:absolute;left:0;right:0;top:150px;bottom:0;border-radius:0 0 22px 22px;background:linear-gradient(170deg,#ebc877,var(--gold));display:flex;align-items:center;justify-content:center">
    <span style="font:900 64px/1 var(--display);letter-spacing:.12em;color:var(--gold-ink)">DOSAR</span>
  </div>
</div>'''

page('03-carusel-1', f'''<div class="frame" style="padding:64px 72px 56px;gap:0">
  <div style="display:flex;align-items:center;gap:28px"><div class="brand" style="flex:1">West Auto Botoșani</div>{dots(0)}</div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:40px">
    <p class="eyebrow">Dosarul mașinii</p>
    <h1 class="h-l">Ce vezi la noi<br>înainte să dai<br><span class="gold">un leu.</span></h1>
    <p class="body-l" style="max-width:820px">Patru lucruri pe care le primești pentru fiecare mașină din parc. Glisează.</p>
  </div>
  {folder}
</div>''')
MANIFEST.append(('03-carusel-1', 1080, 1350, False))

for i in range(1, 5):
    n, title, body, ex_t, ex_p = CARDS[i]
    page(f'03-carusel-{i + 1}', f'''<div class="frame" style="padding:64px 72px 56px;gap:0">
  <div style="display:flex;align-items:center;gap:28px"><div class="brand" style="flex:1">West Auto Botoșani</div>{dots(i)}</div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:40px">
    <span class="num">{n}</span>
    <h2 class="h-m">{E(title)}</h2>
    <p class="body-l">{E(body)}</p>
    <div class="example"><small>Exemplu din parc · {E(ex_t)}</small><p>{E(ex_p)}</p></div>
  </div>
  <div class="foot"><span>Dosarul mașinii</span><span><b>Scrie DOSAR</b> pe WhatsApp · {WA}</span></div>
</div>''')
    MANIFEST.append((f'03-carusel-{i + 1}', 1080, 1350, False))

page('03-carusel-6', f'''<div class="frame" style="padding:64px 72px 56px;gap:0">
  <div style="display:flex;align-items:center;gap:28px"><div class="brand" style="flex:1">West Auto Botoșani</div>{dots(5)}</div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:44px">
    <h2 class="h-l">Cere dosarul<br><span class="gold">oricărei mașini.</span></h2>
    <p class="body-l">Scrie pe WhatsApp cuvântul <b style="color:var(--ink)">DOSAR</b> și modelul care te interesează. Îți trimitem istoricul, raportul și pozele cu actele.</p>
    <div style="display:flex;flex-direction:column;gap:10px">
      <span class="eyebrow" style="color:var(--muted)">WhatsApp</span>
      <span style="font:900 120px/1 var(--display);color:var(--gold);font-variant-numeric:tabular-nums">{WA}</span>
    </div>
  </div>
  <div class="foot"><span>{ADDR}</span><span>Fără povești. <b>Doar acte.</b></span></div>
</div>''')
MANIFEST.append(('03-carusel-6', 1080, 1350, False))

# Grilă cu stocul (6 mașini, doar prețul curent, fără preț tăiat)
GRID = ['sportA', 'qqt', 'tiguan', 'duster', 'clio', 'v40']
cells = ''
for k in GRID:
    c = cars[k]
    cells += f'''<div style="background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column">
  <img src="../poze/{k}.jpg" style="width:100%;height:292px;object-fit:cover;display:block">
  <div style="padding:18px 22px 20px;display:flex;flex-direction:column;gap:8px">
    <b style="font:800 29px/1.1 var(--display)">{E(c["short"])}</b>
    <span style="font:600 23px/1.2 var(--body);color:var(--muted)">{c["year"]} · {c["km"]} km</span>
    <span style="font:900 40px/1 var(--display);color:var(--gold);font-variant-numeric:tabular-nums">{E(c["price"])}</span>
  </div></div>'''
page('04-stoc-feed', f'''<div class="frame" style="padding:60px 64px 52px;gap:30px">
  <div class="brand">West Auto Botoșani</div>
  <h1 class="h-m" style="font-size:58px">Fiecare mașină,<br><span class="gold">cu dosarul ei.</span></h1>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;flex:1;align-content:start">{cells}</div>
  <div class="cta" style="padding:24px 32px"><b style="font-size:34px">Scrie DOSAR + modelul</b><span style="font-size:34px">{WA}</span></div>
</div>''')
MANIFEST.append(('04-stoc-feed', 1080, 1350, False))


# Dosarul fiecărei mașini (1080x1350): reclamă pentru o mașină + imaginea trimisă pe WhatsApp
def dosar(k):
    c = dict(cars[k])
    c['facts'] = [('Pachet Full Self-Driving (FSD) cumpărat; în UE funcțiile disponibile sunt limitate' if 'FSD' in f else f) for f in c['facts']]
    facts = ''.join(f'<li>{E(f)}</li>' for f in c['facts'][:4])
    dot = ''.join(f'<span style="font:600 25px/1.2 var(--body);border:1.5px solid var(--line);border-radius:999px;padding:10px 18px;background:rgba(255,255,255,.04)">{E(d)}</span>'
                  for d in c['dotari'][:4])
    psize = 104 if len(c['price']) <= 7 else 88
    if c['vat']:
        price = f'''<span style="font:900 88px/.95 var(--display);color:var(--gold);font-variant-numeric:tabular-nums;white-space:nowrap">{E(c["price_incl"])}</span>
      <span style="font:700 26px/1.2 var(--body);color:var(--ink)">preț final cu TVA · pentru firme {E(c["price"])} + TVA (deductibil)</span>'''
    else:
        price = f'''<span style="font:900 {psize}px/.95 var(--display);color:var(--gold);font-variant-numeric:tabular-nums;white-space:nowrap">{E(c["price"])}</span>
      <span style="font:700 26px/1.2 var(--body);color:var(--ink)">{E(c["warranty"][0].upper() + c["warranty"][1:])}</span>'''
    rows = [('An', c['year']), ('Kilometri', c['km'] + ' km'), ('Motorizare', c['specs'])]
    table = ''.join(f'<div style="display:flex;flex-direction:column;gap:4px;padding:12px 0;border-top:2px solid var(--paper-line)"><small style="font:800 17px/1 var(--display);letter-spacing:.14em;text-transform:uppercase;color:var(--paper-muted)">{E(a)}</small><b style="font:700 27px/1.2 var(--body)">{E(b)}</b></div>' for a, b in rows)
    page(f'05-dosar-{k}', f'''<div class="frame" style="padding:56px 64px 52px;gap:26px">
  <div style="display:flex;align-items:center;gap:24px"><div class="brand" style="flex:1">West Auto Botoșani</div><span class="eyebrow">Dosarul mașinii</span></div>
  <h1 style="font:900 58px/1.02 var(--display);text-transform:uppercase">{E(c["short"])}</h1>
  <div style="background:var(--paper);color:var(--paper-ink);border-radius:20px;padding:34px 36px 30px;display:flex;flex-direction:column;gap:26px;box-shadow:0 30px 60px rgba(0,0,0,.4);position:relative">
    <span style="position:absolute;top:-22px;right:40px;background:var(--gold);color:var(--gold-ink);font:900 20px/1 var(--display);letter-spacing:.18em;padding:12px 18px;border-radius:8px">DOSAR</span>
    <div style="display:grid;grid-template-columns:478px 1fr;gap:30px;align-items:start">
      <img src="../poze/{k}.jpg" style="width:478px;height:256px;object-fit:cover;border-radius:12px;display:block">
      <div style="display:flex;flex-direction:column">{table}</div>
    </div>
    <div style="display:flex;flex-direction:column;gap:14px">
      <small style="font:800 18px/1 var(--display);letter-spacing:.16em;text-transform:uppercase;color:var(--paper-muted)">Ce e în dosar</small>
      <ul class="checks" style="gap:12px">{facts.replace("<li>", "<li style='font-size:28px;color:var(--paper-ink)'>")}</ul>
    </div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:16px">
    <small style="font:800 18px/1 var(--display);letter-spacing:.16em;text-transform:uppercase;color:var(--muted)">Dotări principale</small>
    <div style="display:flex;flex-wrap:wrap;gap:12px">{dot}</div>
  </div>
  <div style="display:flex;justify-content:space-between;align-items:flex-end;gap:30px">
    <div style="display:flex;flex-direction:column;gap:12px;min-width:0">{price}</div>
    <div style="text-align:right;display:flex;flex-direction:column;gap:8px;flex:none">
      <span style="font:800 24px/1 var(--display);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)">Scrie DOSAR pe WhatsApp</span>
      <span style="font:900 46px/1 var(--display);font-variant-numeric:tabular-nums">{WA}</span>
    </div>
  </div>
</div>''')
    MANIFEST.append((f'05-dosar-{k}', 1080, 1350, False))


for k in cars:
    dosar(k)

# Cadru final pentru clipuri (1080x1920) și eticheta de serie (PNG transparent, se pune peste video)
page('06-video-final', f'''<div class="frame" style="padding:260px 80px 420px;justify-content:center;gap:56px">
  <div class="brand">West Auto Botoșani</div>
  <h1 class="h-xl fitbox" style="font-size:150px"><span>Fără povești.</span><span class="gold">Doar acte.</span></h1>
  <p class="body-l" style="font-size:46px">Cere dosarul oricărei mașini din parc. Îl primești pe WhatsApp.</p>
  <div class="cta"><b>Scrie DOSAR<br>pe WhatsApp</b><span style="font-size:44px">{WA}</span></div>
  <p class="muted" style="font:600 30px/1.3 var(--body)">{ADDR}</p>
</div>''')
MANIFEST.append(('06-video-final', 1080, 1920, False))

page('07-video-eticheta', '''<div style="position:absolute;left:64px;top:220px;display:flex;align-items:center;gap:14px;
  background:rgba(14,16,19,.82);border:2px solid var(--gold);border-radius:999px;padding:16px 28px 16px 22px">
  <i style="width:18px;height:18px;border-radius:50%;background:var(--gold)"></i>
  <span style="font:900 34px/1 var(--display);letter-spacing:.08em;text-transform:uppercase">Fără povești</span>
</div>''', cls='clear')
MANIFEST.append(('07-video-eticheta', 1080, 1920, True))

# Copertă pagină Facebook (1640x624; pe telefon se vede doar centrul de ~1200 px)
page('08-coperta-facebook', f'''<div class="frame" style="padding:0 220px;justify-content:center;gap:30px">
  <div class="brand" style="font-size:20px">West Auto Botoșani · {ADDR}</div>
  <h1 class="h-xl" style="font-size:104px">Fără povești. <span class="gold">Doar acte.</span></h1>
  <p class="body-l" style="font-size:34px">Fiecare mașină din parc are dosarul ei. Scrie <b style="color:var(--ink)">DOSAR</b> pe WhatsApp: {WA}</p>
</div>''')
MANIFEST.append(('08-coperta-facebook', 1640, 624, False))

json.dump(MANIFEST, open('manifest.json', 'w'))
print(len(MANIFEST), 'vizuale')
