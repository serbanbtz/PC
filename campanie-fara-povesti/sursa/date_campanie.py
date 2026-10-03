# Sursa unică pentru partea executabilă a campaniei „Fără povești”:
# calendar, texte (reclame, postări, TikTok, WhatsApp), scripturi video și pașii de lansare.
# Rulează:  python3 date_campanie.py   → scrie ../campanie.json și documentele 03–06 (.md)
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
cars = {c['key']: c for c in json.load(open(os.path.join(HERE, 'cars.json')))}

WA = '0771 311 941'
WA_LINK = 'https://wa.me/40771311941'
ADR = 'Bd. Mihai Eminescu 2A, Botoșani, lângă Kaufland Gară'

# ---------------------------------------------------------------- Reclame Meta
RECLAME = {
    'texte_principale': [
        {'id': 'T1', 'nume': 'Manifest', 'text':
         f'„A fost a unui neamț bătrân.” „A plâns când a vândut-o.” „Km reali, pe cuvânt.”\n\n'
         f'Le-ai auzit și tu. La West Auto nu auzi povești, vezi actele.\n\n'
         f'Fiecare mașină din parc are dosarul ei: istoric de service și facturi, raport pe seria de șasiu, '
         f'kilometri pe care îi poți verifica, test drive și 12 luni garanție în scris.\n\n'
         f'👉 Apasă „Trimite mesaj”, scrie DOSAR și modelul care te interesează. Îți trimitem dosarul pe WhatsApp.\n'
         f'📍 {ADR}'},
        {'id': 'T2', 'nume': 'Scurt', 'text':
         'Înainte să dai un leu pe o mașină second-hand, cere-i dosarul.\n\n'
         'La noi îl primești pe WhatsApp pentru oricare mașină din parc: istoricul, raportul și pozele cu actele. '
         'Scrie DOSAR și modelul.\n\n'
         f'📍 {ADR}'},
        {'id': 'T3', 'nume': 'Iarna', 'text':
         'Iarna se cumpără SUV-ul, nu povestea lui.\n\n'
         '4x4, Webasto, scaune încălzite: le vezi la test drive. Istoricul, facturile și raportul pe seria de șasiu '
         'le vezi în dosar, înainte să vii.\n\n'
         '👉 Scrie DOSAR și modelul pe WhatsApp.\n'
         f'📍 {ADR}'},
    ],
    'titluri': ['Fără povești. Doar acte.', 'Cere dosarul mașinii pe WhatsApp', 'Mașini cu istoric, în Botoșani',
                'SUV pentru iarnă, cu dosar complet', 'Vezi actele înainte de test drive'],
    'descriere': 'West Auto Botoșani · Bd. Mihai Eminescu 2A',
    'mesaj_precompletat_general': 'Bună! Vreau DOSARUL unei mașini. Mă interesează: ',
}


def text_dosar_reclama(k):
    c = cars[k]
    fapte = '\n'.join('✅ ' + f for f in c['facts'][:4])
    return (f'{c["short"]}, {c["year"]} · {c["price"]}\n\nCe e în dosar:\n{fapte}\n\n'
            f'Cere dosarul complet pe WhatsApp înainte să vii la test drive. Fără povești, doar acte.\n📍 {ADR}')


RECLAME['dosare'] = [{'masina': k, 'nume': cars[k]['short'], 'vizual': f'05-dosar-{k}.png',
                      'text': text_dosar_reclama(k),
                      'mesaj_precompletat': f'Bună! Vreau DOSARUL pentru {cars[k]["short"]}.'}
                     for k in ['sportA', 'qqt', 'tiguan', 'duster']]

STRUCTURA = [
    {'nivel': 'Campanie', 'nume': 'WA | Fără povești | oct 2026',
     'setari': ['Obiectiv: Interacțiune (Engagement)', 'Locul conversației: Aplicații de mesagerie → WhatsApp',
                'Categorii speciale de reclame: niciuna (reclamele nu vorbesc despre rate sau credit)',
                'Buget pe set de reclame (nu Advantage+ campaign budget), ca să controlezi fiecare public',
                'Test A/B: nu']},
    {'nivel': 'Set A', 'nume': 'A · Local 40 km · Încredere', 'buget': '25 lei/zi',
     'setari': ['Număr WhatsApp: 0771 311 941 (legat de pagină)', 'Obiectiv de performanță: Maximizează numărul de conversații',
                'Locație: Botoșani + 40 km (persoane care locuiesc aici sau au fost recent)', 'Vârstă: 24–60 de ani, toate genurile',
                'Public Advantage+: oprit (folosești opțiunile de public de mai sus)',
                'Plasamente manuale: Facebook Feed, Reels, Stories, Marketplace; Instagram Feed, Reels, Stories. Fără Audience Network și Messenger',
                'Program: start miercuri 7 oct, 06:00; fără dată de final (o oprești pe 1 nov)'],
     'reclame': ['A1 Manifest: 01-manifest-feed.png (feed) + 02-manifest-story.png (Stories/Reels), text T1, titlu „Fără povești. Doar acte.”',
                 'A2 Carusel: 03-carusel-1…6.png, text T2, titlu „Cere dosarul mașinii pe WhatsApp”',
                 'A3 Stoc: 04-stoc-feed.png, text T2, titlu „Mașini cu istoric, în Botoșani”',
                 'A4 (din 12 oct) Video „Povești de parc” (V1), text T1']},
    {'nivel': 'Set B', 'nume': 'B · Botoșani, Suceava, Iași · SUV de iarnă', 'buget': '15 lei/zi',
     'setari': ['Același număr de WhatsApp și același obiectiv de performanță',
                'Locație: Botoșani + 40 km, Suceava + 25 km, Iași + 25 km (adaugi cele trei orașe; Meta nu acceptă o rază mai mare de 80 km)', 'Vârstă: 27–60 de ani', 'Aceleași plasamente ca la A'],
     'reclame': ['B1 Dosar Kia Sportage 4x4 automat (05-dosar-sportA.png)', 'B2 Dosar Nissan Qashqai automat (05-dosar-qqt.png)',
                 'B3 Dosar VW Tiguan 4Motion (05-dosar-tiguan.png)', 'B4 Dosar Dacia Duster (05-dosar-duster.png)',
                 'Text: textul fiecărui dosar de mai jos sau T3; mesaj precompletat cu modelul mașinii',
                 'Din 12 oct: B5–B6 video „Dosarul în 15 secunde” (V2) pentru Sportage și Tiguan']},
    {'nivel': 'Set C', 'nume': 'C · Retargeting 30 de zile', 'buget': '10 lei/zi, din 26 oct',
     'setari': ['Public personalizat: persoane care au interacționat cu pagina sau cu reclamele în ultimele 30 de zile + cei care au văzut 50% din clipuri',
                'Exclude: persoanele care ți-au scris deja pe WhatsApp (dacă Meta oferă publicul de conversații)',
                'Locație: aceleași trei orașe ca la setul B'],
     'reclame': ['Dosarele mașinilor rămase în stoc (maximum 4), text „Ai văzut-o deja. Vino s-o conduci: test drive cu dosarul la vedere.”']},
]

BUGET = [
    {'varianta': 'Minim', 'meta': '30 lei/zi doar setul A (≈ 780 lei pentru 26 de zile)', 'tiktok': '0 lei', 'total': '≈ 780 lei',
     'cand': 'Dacă vrei doar să testezi conceptul.'},
    {'varianta': 'Recomandat', 'meta': 'A 25 + B 15 lei/zi, apoi + C 10 lei/zi din 26 oct (≈ 1.110 lei)',
     'tiktok': '3 promovări × 90 lei (≈ 270 lei)', 'total': '≈ 1.380 lei', 'cand': 'Planul pe care e construit calendarul.'},
    {'varianta': 'Accelerat', 'meta': '70 lei/zi (≈ 1.820 lei)', 'tiktok': '6 promovări × 90 lei (≈ 540 lei)', 'total': '≈ 2.360 lei',
     'cand': 'Doar după ce costul pe conversație e sub 20 lei două săptămâni la rând.'},
]

# ---------------------------------------------------------------- Postări organice


def text_dosar_postare(k):
    c = cars[k]
    fapte = '\n'.join('✅ ' + f for f in c['facts'])
    pret = f'{c["price_incl"]} cu TVA ({c["price"]} + TVA pentru firme, TVA deductibil)' if c['vat'] else c['price']
    dot = ' · '.join(c['dotari'][:4])
    return (f'📁 Dosarul săptămânii: {c["short"]}, {c["year"]}\n\n{c["specs"]}\n\nCe e în dosar:\n{fapte}\n\n'
            f'Dotări: {dot}\n\n💰 {pret}\n🛡️ {c["warranty"][0].upper() + c["warranty"][1:]}\n\n'
            f'Vrei tot dosarul (istoric, raport, poze cu actele)? Scrie DOSAR pe WhatsApp: {WA_LINK}\n📍 {ADR}\n\n'
            f'❓ Ce ai vrea să vezi în dosarul unei mașini înainte s-o cumperi? Scrie-ne în comentarii.\n\n'
            f'#WestAuto #Botosani #FaraPovesti')


POSTARI = {
    'P1': {'nume': 'Manifestul (lansare)', 'vizual': '01-manifest-feed.png', 'text':
           'Am auzit toți poveștile. „A fost a unui neamț bătrân.” „Mergea doar duminica.” „Km reali, pe cuvânt.” 🙂\n\n'
           'De azi, la West Auto le înlocuim cu ceva mai simplu: un dosar pentru fiecare mașină din parc.\n\n'
           '📁 Ce e în dosar:\n✅ istoricul de service și facturile\n✅ raportul de istoric pe seria de șasiu\n'
           '✅ kilometrii, ca să-i compari singur\n✅ 12 luni garanție, în scris\n\nȘi test drive înainte de orice decizie.\n\n'
           f'Vrei dosarul unei mașini? Scrie DOSAR și modelul pe WhatsApp: {WA_LINK}\n📍 {ADR}\n\n'
           '❓ Care e cea mai tare poveste pe care ai auzit-o când ți-ai cumpărat mașina? Scrie-o în comentarii 👇\n\n'
           '#WestAuto #Botosani #FaraPovesti'},
    'P2': {'nume': 'Carusel „Ce e în dosar”', 'vizual': '03-carusel-1…6.png', 'text':
           'Ce vezi la noi înainte să dai un leu 👉 glisează.\n\n'
           '1. Istoricul de service: ce s-a schimbat și când, cu facturi.\n2. Raportul de istoric pe seria de șasiu.\n'
           '3. Kilometrii, pe care îi compari singur cu cartea de service.\n4. Garanția de 12 luni, scrisă în contract.\n\n'
           f'Alege orice mașină din parc și cere-i dosarul: scrie DOSAR pe WhatsApp la {WA_LINK}\n📍 {ADR}\n\n'
           '#WestAuto #Botosani #FaraPovesti'},
    'P3': {'nume': 'Stocul cu dosar', 'vizual': '04-stoc-feed.png', 'text':
           'Fiecare mașină din parc, cu dosarul ei 📁\n\nKia Sportage 4x4 automat · Nissan Qashqai automat · VW Tiguan 4Motion · '
           'Dacia Duster · Renault Clio · Volvo V40 și alte mașini în parc.\n\n'
           f'Spune-ne ce model te interesează și îți trimitem dosarul: istoric, raport, poze cu actele.\n📲 {WA_LINK}\n📍 {ADR}\n\n'
           '❓ Pe care ai alege-o tu? Scrie modelul în comentarii.\n\n#WestAuto #Botosani #FaraPovesti'},
    'P4': {'nume': 'Pregătite de iarnă (carusel)', 'vizual': '05-dosar-sportA.png + 05-dosar-sportM.png + 05-dosar-tiguan.png', 'text':
           'Pregătite de iarnă, cu dosar complet ❄️\n\nTrei SUV-uri 4x4 din parc, cu istoricul lor la vedere: Kia Sportage automat '
           '(cu Webasto), Kia Sportage manual și VW Tiguan 4Motion. Glisează pentru dosarul fiecăruia.\n\n'
           f'Scrie DOSAR și modelul pe WhatsApp: {WA_LINK}\n📍 {ADR}\n\n#WestAuto #Botosani #FaraPovesti'},
    'P5': {'nume': 'Reel „Povești de parc” (V1)', 'vizual': 'video V1', 'text':
           'Poveștile le știm cu toții 🙂 La noi primești altceva: dosarul mașinii.\n\n'
           f'Cere-l pentru orice mașină din parc: scrie DOSAR pe WhatsApp la {WA_LINK}\n\n'
           '❓ Ce poveste ai auzit tu? Scrie-o în comentarii.\n\n#WestAuto #Botosani #FaraPovesti'},
    'P6': {'nume': 'Vândute', 'vizual': 'video sau poză de la predare (doar cu acordul clientului)', 'text':
           'Încă o mașină a plecat acasă, cu dosarul ei 🔑 Mulțumim pentru încredere!\n\n'
           f'Următoarea poate fi a ta. Scrie DOSAR pe WhatsApp: {WA_LINK}\n\n#WestAuto #Botosani #FaraPovesti'},
}
for k in cars:
    POSTARI['D-' + k] = {'nume': f'Dosarul săptămânii: {cars[k]["short"]}', 'vizual': f'05-dosar-{k}.png', 'text': text_dosar_postare(k)}

TIKTOK = {
    'bio': f'Mașini second-hand cu dosar complet 📁 Scrie DOSAR pe WhatsApp: {WA} · Bd. Mihai Eminescu 2A, Botoșani',
    'hashtaguri': '#botosani #suceava #iasi #masinisecondhand #parcauto #FaraPovesti #WestAuto',
    'descrieri': {
        'manifest': 'Fără povești. Doar acte. 📁 Fiecare mașină din parc are dosarul ei. Scrie DOSAR pe WhatsApp: 0771 311 941',
        'V1': 'Le știi pe toate? 😅 La noi primești dosarul mașinii. Ce poveste ai auzit tu? 👇',
        'V2': '{Model} · {preț}. Ăsta e dosarul lui, în 15 secunde. Scrie DOSAR pe WhatsApp: 0771 311 941',
        'V3': 'POV: suni la un anunț 📞 Între timp, la West Auto… 📁',
        'V4': 'Răspuns la comentariu: am adus actele 📁',
        'V5': 'Pornire la rece, fără povești ❄️ Ce zici de sunetul ăsta?',
        'iarna': '3 SUV-uri 4x4 pregătite de iarnă, cu dosar. Pe care o alegi: 1, 2 sau 3? 👇',
    },
}

WHATSAPP = {
    'etichete': ['DOSAR · reclamă FB', 'DOSAR · TikTok', 'DOSAR · organic', 'OCTOMBRIE', 'Test drive programat', 'Vândut'],
    'salut': ('Bună, aici West Auto Botoșani! 👋 Spune-ne ce mașină te interesează și îți trimitem dosarul ei: '
              'istoricul de service, raportul pe seria de șasiu și pozele cu actele.'),
    'absent': ('Mulțumim că ne-ai scris! Acum suntem închiși. Mâine dimineață îți răspundem printre primii. '
               'Până atunci, spune-ne ce mașină te interesează.'),
    'rapide': [
        {'cod': '/dosar', 'text': ('Mulțumim! Îți trimit acum dosarul pentru [mașina]: fișa mașinii, istoricul de service și raportul de istoric. '
                                   'Dacă ai întrebări după ce te uiți pe el, sunt aici. Vrei să vii și la un test drive?')},
        {'cod': '/testdrive', 'text': ('Super! Ce zi și ce oră ți se potrivesc? Pregătim mașina și dosarul la vedere. '
                                       f'Ne găsești pe {ADR}. Ia cu tine buletinul și permisul.')},
        {'cod': '/rate', 'text': ('Se poate și în rate, cu avans de la 0. Ca să-ți calculăm rata, spune-ne suma, pe câte luni '
                                  'și dacă ai venit din salariu sau din firmă/PFA.')},
        {'cod': '/locatie', 'text': f'Ne găsești pe {ADR}. [link Google Maps]'},
        {'cod': '/vandut', 'text': ('Mașina asta s-a vândut chiar zilele trecute. Ce buget ai și ce cauți? '
                                    'Îți trimit dosarele mașinilor apropiate din parc.')},
    ],
    'comentarii': [
        {'cand': 'Preț?', 'raspuns': 'Prețul e în descriere. Îți trimitem și dosarul complet pe WhatsApp: scrie DOSAR la 0771 311 941.'},
        {'cand': 'Mai e disponibilă?', 'raspuns': 'Da, e încă în parc. Scrie DOSAR pe WhatsApp la 0771 311 941 și îți trimitem tot.'},
        {'cand': 'Se poate în rate?', 'raspuns': 'Da, cu avans de la 0. Scrie-ne pe WhatsApp la 0771 311 941 și îți calculăm rata.'},
        {'cand': '„Sigur e dată înapoi la km”', 'raspuns': ('Întrebare corectă. De asta are dosar: carte service și raport pe seria de șasiu. '
                                                          'Ți le trimitem pe WhatsApp (0771 311 941) și le verifici singur.')},
        {'cand': 'E accidentată?', 'raspuns': 'Raportul de istoric arată daunele declarate. Îl primești pe WhatsApp: scrie DOSAR la 0771 311 941.'},
        {'cand': 'De unde e adusă?', 'raspuns': 'Țara de proveniență e trecută în dosar. Scrie DOSAR pe WhatsApp și ți-l trimitem.'},
        {'cand': 'Comentariu răutăcios', 'raspuns': 'Mulțumim de comentariu. Dosarul e la dispoziția oricui vrea să verifice.'},
    ],
}

# ---------------------------------------------------------------- Scripturi video
VIDEO = [
    {'id': 'V1', 'titlu': 'Povești de parc', 'durata': '20–25 s', 'rol': 'Clipul principal: reclamă (set A) și TikTok/Reels',
     'cine': 'Prezentatorul West Auto + un prieten care joacă „vânzătorul cu povești” (ochelari de soare, sprijinit de capotă)',
     'cadre': [
         ('0–2 s', '„Vânzătorul”, plan apropiat, lângă o mașină: „A fost a unui neamț bătrân…”', 'CE AUZI LA MAȘINI SECOND-HAND'),
         ('2–4 s', 'Același, mai convins: „…a plâns când a vândut-o.”', ''),
         ('4–6 s', 'Bate cu palma în capotă: „Km reali, pe cuvânt!”', ''),
         ('6–7 s', 'Imaginea îngheață (efect în montaj); prezentatorul intră în cadru și clatină din cap.', ''),
         ('7–15 s', 'Prezentatorul pune un dosar pe capotă și îl deschide: cartea de service (filă cu filă), o factură, telefonul cu raportul, bordul la pornire cu kilometrajul.',
          'CARTE SERVICE · RAPORT PE SERIA DE ȘASIU · KM VERIFICABILI'),
         ('15–20 s', 'Prezentatorul, în cameră: „La noi nu auzi povești. Vezi actele. Cere dosarul oricărei mașini.”', 'FĂRĂ POVEȘTI. DOAR ACTE.'),
         ('20–23 s', 'Cadrul final (06-video-final.png).', 'SCRIE DOSAR PE WHATSAPP · 0771 311 941'),
     ],
     'varianta': 'Dacă nu ai pe cineva pentru rolul de „vânzător”: prezentatorul citește poveștile de pe telefon, ca pe niște comentarii, râde, apoi deschide dosarul.',
     'sunet': 'Fără muzică în primele 6 secunde (se aude vocea), apoi un sunet în trend, încet.'},
    {'id': 'V2', 'titlu': 'Dosarul în 15 secunde', 'durata': '15 s', 'rol': 'Serie: câte un clip pe mașină; reclamă în setul B',
     'cine': 'Doar mâinile prezentatorului și, opțional, vocea lui',
     'cadre': [
         ('0–2 s', 'Mașina, față ¾ de jos (cadrul 1 din schema de filmare).', '{MODEL} · {PREȚ} · ÎȚI ARĂT DOSARUL'),
         ('2–5 s', 'Dosarul pe capotă se deschide; cartea de service cu ștampilele (numele fostului proprietar acoperit).', 'CARTE SERVICE'),
         ('5–8 s', 'O factură sau piesa schimbată (ex.: kit transmisie nou).', 'CE S-A SCHIMBAT'),
         ('8–11 s', 'Telefonul cu raportul (CarVertical sau RAR), derulat încet; seria de șasiu parțial acoperită.', 'RAPORT PE SERIA DE ȘASIU'),
         ('11–13 s', 'Bordul la pornire, cu kilometrajul.', '{KM} KM'),
         ('13–15 s', 'Cadrul final.', 'SCRIE DOSAR PE WHATSAPP'),
     ],
     'varianta': 'Voce (opțional): „{Model}, {preț} euro. Ăsta e dosarul lui. Scrie DOSAR și ți-l trimitem.”',
     'sunet': 'Sunet în trend, ritmat; tăieturile cad pe ritm.'},
    {'id': 'V3', 'titlu': 'POV: suni la un anunț', 'durata': '15–18 s', 'rol': 'TikTok, pentru distribuiri și comentarii',
     'cine': 'Prezentatorul, singur',
     'cadre': [
         ('0–3 s', 'Prezentatorul la telefon, plictisit, dă din cap.', 'POV: SUNI LA UN ANUNȚ'),
         ('3–8 s', 'Pe ecran apar pe rând replicile din telefon; el își dă ochii peste cap la fiecare.', '„NEAMȚ BĂTRÂN” · „DOAR LA BISERICĂ” · „NU ARE NIMIC”'),
         ('8–10 s', 'Închide telefonul.', 'ÎNTRE TIMP, LA WEST AUTO:'),
         ('10–15 s', 'Dosarul trântit pe capotă, se deschide; zâmbește în cameră.', 'FĂRĂ POVEȘTI. DOAR ACTE.'),
     ],
     'varianta': 'Merge și cu un sunet de tip „dialog” din trenduri, peste care pui replicile ca text.',
     'sunet': 'Un sunet amuzant din „Trending”.'},
    {'id': 'V4', 'titlu': 'Răspuns la comentariu', 'durata': '15–25 s', 'rol': 'TikTok: transformă suspiciunea în dovadă',
     'cine': 'Prezentatorul, lângă mașina din comentariu',
     'cadre': [
         ('0–2 s', 'În TikTok: „Răspunde cu un videoclip” la un comentariu de tipul „sigur e dată înapoi la km”. Comentariul apare automat pe ecran.', ''),
         ('2–15 s', 'Prezentatorul deschide dosarul acelei mașini: cartea de service, raportul pe telefon, bordul.', 'AM ADUS ACTELE'),
         ('15–20 s', '„Le vrei pe toate? Scrie DOSAR pe WhatsApp.”', 'SCRIE DOSAR · 0771 311 941'),
     ],
     'varianta': 'Alege comentarii politicoase sau neutre; nu răspunde ironic.',
     'sunet': 'Vocea, fără muzică sau cu muzică foarte încet.'},
    {'id': 'V5', 'titlu': 'Pornire la rece, fără povești', 'durata': '10–12 s', 'rol': 'Toamnă–iarnă: diesel și 4x4',
     'cine': 'Nimeni în cadru; dimineața devreme, mașina a stat afară peste noapte',
     'cadre': [
         ('0–2 s', 'Bordul: temperatura de afară pe afișaj.', 'PORNIRE LA RECE · {X}°C'),
         ('2–8 s', 'Capota deschisă, pornirea, motorul la ralanti; apoi țeava de eșapament.', 'FĂRĂ POVEȘTI'),
         ('8–12 s', 'Cadrul final.', '{MODEL} · DOSAR PE WHATSAPP'),
     ],
     'varianta': 'Filmează doar mașini care pornesc curat; un clip cu fum sau zgomote face mai mult rău decât bine.',
     'sunet': 'Doar sunetul motorului.'},
]

# ---------------------------------------------------------------- Calendar (4 oct – 2 nov)
# fiecare zi: (data, fază, Facebook 19:00, TikTok 18:00, reclame, tu / echipa)
CAL = [
    ('2026-10-04', 0, 'Programate deja: Kangoo 09:00, Volvo V40 13:00, Sportage manual 19:00', 'Toyota C-HR (montat, din planul vechi)', '',
     'Citești planul și aprobi conceptul, vizualele și bugetul (30 min). Notezi ce mașini s-au vândut.'),
    ('2026-10-05', 0, 'Programat deja: Seat Toledo 09:00. Seara: Reel Duster (planul vechi)', 'Audi A6 Avant narat (montat)', '',
     'În Ads Manager: verificarea identității de advertiser, metoda de plată, WhatsApp legat de pagină (30 min). Reclama „OCTOMBRIE” rămâne schiță.'),
    ('2026-10-06', 0, 'Reel Tesla Model 3 (planul vechi)', 'Peugeot 207 SW (montat)', 'Seara: campania „Fără povești” publicată, cu start miercuri la 06:00',
     'WhatsApp Business: mesaje rapide și etichete (20 min). Programezi postările 7–16 oct. Pregătești pozele cu actele pentru cele 4 mașini din setul B.'),
    ('2026-10-07', 1, 'P1 Manifestul (01-manifest-feed) + fixat sus pe pagină. Coperta nouă (08)', 'Postare foto: manifest + caruselul cu dosarul (02, 03-2…6)',
     'Pornesc seturile A și B. Nu modifici nimic 72 de ore.', 'Răspuns la mesajele DOSAR în sub 15 minute (tu sau cineva din echipă).'),
    ('2026-10-08', 1, 'P2 Carusel „Ce e în dosar” (03-carusel-1…6)', 'Clipul existent Audi A6 automat + eticheta „Fără povești” + cadrul final', 'Doar verifici că reclamele rulează',
     'Ziua interviului: WhatsApp-ul îl preia cineva din echipă.'),
    ('2026-10-09', 1, 'D Dosarul săptămânii: Kia Sportage 4x4 automat', 'Postare foto: 3 SUV-uri de iarnă cu dosar (Sportage automat, Tiguan, Qashqai automat)', '',
     'Salvezi cele mai bune „povești” din comentarii, pentru clipurile de luni.'),
    ('2026-10-10', 1, 'P3 Stocul cu dosar (04-stoc-feed)', 'Tur prin parc (filmat dimineață)', '',
     'FILMARE #1, cca 90 min: V1, V2 pentru Sportage automat, Qashqai automat, Tiguan și Duster, V5, cadrele standard pentru Tiguan și Sportage manual, turul parcului.'),
    ('2026-10-11', 1, 'Reel „Pornire la rece” (V5)', 'V5 Pornire la rece, fără povești', '', 'Răspunzi la comentarii în prima oră după 18:00.'),
    ('2026-10-12', 2, 'P5 Reel „Povești de parc” (V1)', 'V1 Povești de parc (clipul principal al campaniei)',
     'Verificarea săptămânii 1. Adaugi V1 în setul A și V2 Sportage/Tiguan în B. Oprești reclama cu cel mai mare cost pe conversație.', 'Verificarea de luni (15 min).'),
    ('2026-10-13', 2, 'D Dosar: Nissan Qashqai automat', 'V2 Dosarul în 15 secunde: Kia Sportage 4x4 automat',
     'TikTok Promote pe cel mai bun clip din săptămâna 1 (30 lei/zi, 3 zile)', ''),
    ('2026-10-14', 2, 'Reel V2 Kia Sportage', 'A sau B? Tiguan 4Motion vs Sportage manual', '', ''),
    ('2026-10-15', 2, 'D Dosar: VW Tiguan 4Motion', 'V2 Dosarul în 15 secunde: VW Tiguan', 'Verificare la jumătatea lunii', ''),
    ('2026-10-16', 2, 'P6 Vândute (dacă s-a vândut) sau D Dosar: Dacia Duster', 'Vândute sau V2 Dosar Dacia Duster', '', ''),
    ('2026-10-17', 2, 'Stocul actualizat (04-stoc-feed refăcut fără mașinile vândute)', 'Tur prin parc', '',
     'FILMARE #2, cca 60 min: V3, V2 pentru Clio, V40 și Qashqai+2, două V4 (răspunsuri la comentarii), turul parcului.'),
    ('2026-10-18', 2, 'D Dosar: Volvo V40', 'V2 Dosar Nissan Qashqai automat', '', ''),
    ('2026-10-19', 2, 'Reel V3 „POV: suni la un anunț”', 'V3 POV: suni la un anunț',
     'Verificarea săptămânii 2. Scoți reclamele mașinilor vândute; pui V2 nou dacă a mers.', 'Verificarea de luni (15 min).'),
    ('2026-10-20', 2, 'D Dosar: Renault Clio', 'V4 Răspuns la comentariu #1', 'TikTok Promote pe cel mai bun clip din săptămâna 2', ''),
    ('2026-10-21', 2, 'Reel V2 Volvo V40', 'V2 Dosar Volvo V40', '', ''),
    ('2026-10-22', 2, 'D Dosar: Nissan Qashqai+2, 7 locuri', 'V2 Dosar Qashqai+2 („pentru familie”)', '', ''),
    ('2026-10-23', 2, 'P6 Vândute sau D Dosar: Renault Scenic', 'V4 #2 sau Vândute', '', ''),
    ('2026-10-24', 2, 'Stocul actualizat', 'Tur prin parc', '',
     'FILMARE #3, cca 60 min: „Povești de parc” episodul 2, încă un V5, clipul „Gata de iarnă” (Webasto, 4x4, anvelope), V2 pentru mașinile nou intrate.'),
    ('2026-10-25', 2, 'Reel V2 Renault Clio', 'V2 Dosar Renault Clio', '', ''),
    ('2026-10-26', 3, 'Reel „Gata de iarnă”', '„Gata de iarnă”: 3 SUV-uri cu dosar', 'Verificarea săptămânii 3. Pornești setul C (retargeting, 10 lei/zi).', 'Verificarea de luni (15 min).'),
    ('2026-10-27', 3, 'D Dosar: SEAT Arona', 'Ghicește prețul (Arona)', 'TikTok Promote pe cel mai bun clip din săptămâna 3', ''),
    ('2026-10-28', 3, 'Reel „Povești de parc” ep. 2', '„Povești de parc” ep. 2', '', ''),
    ('2026-10-29', 3, 'P4 Pregătite de iarnă (carusel cu 3 dosare 4x4)', 'V5 Pornire la rece #2', '', ''),
    ('2026-10-30', 3, 'Recapitularea lunii: mașinile vândute', 'Vândute: recapitularea lunii', '', ''),
    ('2026-10-31', 3, 'Stocul actualizat', 'Tur prin parc', '', 'FILMARE #4, pentru noiembrie.'),
    ('2026-11-01', 3, 'D Dosar: mașina cu cele mai multe întrebări în octombrie', 'Cel mai bun format al lunii, cu o mașină nouă', 'Ultima zi a primului val', ''),
    ('2026-11-02', 4, '', '', 'Raportul final al campaniei', 'Raportul + planul pentru noiembrie (Black Friday e pe 27 noiembrie). 30 min cu mine.'),
]
FAZE = {0: 'Pregătire', 1: 'Lansare', 2: 'Amplificare', 3: 'Conversie', 4: 'Raport'}
CALENDAR = [dict(data=d, faza=FAZE[f], facebook=fb, tiktok=tt, reclame=ad, tu=tu) for d, f, fb, tt, ad, tu in CAL]

# ---------------------------------------------------------------- Pașii de lansare
PASI = [
    {'etapa': 'Aprobări (duminică 4 oct)', 'pasi': [
        'Aprobi conceptul „Fără povești. Doar acte.” și cuvântul DOSAR pe WhatsApp.',
        'Aprobi vizualele din folderul vizuale/ (sau îmi spui ce schimb).',
        'Alegi bugetul: Minim, Recomandat sau Accelerat.',
        'Alegi prezentatorul clipurilor (recomandarea mea: persoana care va conduce zi de zi parcul).',
        'Confirmi stocul: ce mașini s-au vândut ies din reclame și din calendar.',
        'Confirmi că fiecare mașină din reclame are dosarul pregătit: poze cu cartea de service și facturile (cu datele fostului proprietar acoperite) și raportul pe seria de șasiu.']},
    {'etapa': 'Meta: contul de reclame (luni 5 oct, 30 min)', 'pasi': [
        'business.facebook.com → Setări → Conturi de reclame: verifici că West-Auto Botoșani are cont de reclame în RON.',
        'Ads Manager: dacă apare bannerul „Confirmă cine se află în spatele reclamelor”, completezi verificarea cu buletinul. Poate dura până la 48 de ore, de aceea o faci luni.',
        'Ads Manager → Facturare și plăți: adaugi cardul firmei.',
        'Pagina West-Auto Botoșani → Setări → Conturi conectate → WhatsApp: conectezi 0771 311 941 (primești un cod pe WhatsApp).',
        'Reclama veche „OCTOMBRIE” rămâne schiță. Dacă rulează deja, o oprești miercuri dimineață, când pornește campania nouă.']},
    {'etapa': 'WhatsApp Business (marți 6 oct, 20 min)', 'pasi': [
        'Instrumente pentru afaceri → Mesaj de bun venit: lipești textul „salut” de mai jos.',
        'Instrumente pentru afaceri → Mesaj de absență: lipești textul „absent”, cu programul vostru.',
        'Instrumente pentru afaceri → Răspunsuri rapide: adaugi /dosar, /testdrive, /rate, /locatie, /vandut.',
        'Etichete: creezi etichetele din listă și le pui pe fiecare conversație nouă.',
        'Pe telefon: un album „DOSARE” cu câte un subfolder pe mașină (imaginea 05-dosar-…png + pozele cu actele + raportul PDF).']},
    {'etapa': 'Meta: campania de reclame (marți 6 oct, 40 min)', 'pasi': [
        'Ads Manager → Creează → Interacțiune → Continuă. Nume: „WA | Fără povești | oct 2026”.',
        'Categorii speciale: niciuna. Bugetul campaniei Advantage+: oprit.',
        'Setul A: setările din tabelul „Structura”. Locul conversației: Aplicații de mesagerie → WhatsApp. Obiectiv: maximizează conversațiile.',
        'Reclama A1: format Imagine. Încarci 01-manifest-feed.png, iar la „Personalizare per plasament” pui 02-manifest-story.png pentru Stories și Reels.',
        'Text principal T1, titlu „Fără povești. Doar acte.”, buton „Trimite mesaj pe WhatsApp”. Șablonul de mesaj: textul precompletat de mai jos.',
        'Oprești „Îmbunătățirile creative Advantage+” (Meta poate altfel să adauge muzică sau să schimbe textul).',
        'Reclama A2: format Carusel cu cele 6 cadre 03-carusel-1…6, text T2. Reclama A3: 04-stoc-feed.png, text T2.',
        'Setul B: duplici setul A, schimbi numele, locațiile (Botoșani + 40 km, Suceava + 25 km, Iași + 25 km), vârsta și bugetul. Ștergi reclamele copiate și creezi B1–B4 cu dosarele și mesajul precompletat cu modelul.',
        'Programul: start miercuri 7 oct la 06:00. Publici marți seara; aprobarea Meta vine de obicei în câteva ore.',
        'După aprobare: deschizi fiecare reclamă din „Previzualizare” pe telefon și apeși butonul, ca să vezi că deschide WhatsApp-ul corect.']},
    {'etapa': 'Postările Facebook (marți 6 oct, 30 min)', 'pasi': [
        'Meta Business Suite → Planificator → Creează postare. Alegi doar pagina West-Auto Botoșani.',
        'Încarci imaginea (sau toate cele 6 imagini, în ordine, pentru carusel), lipești textul postării, apeși săgeata de lângă „Publică” → Programează → data și ora din calendar.',
        'Programezi zilele 7–16 octombrie acum, iar restul în fiecare luni, după ce știi ce mașini s-au vândut.',
        'Miercuri 7 oct, după 19:00: deschizi postarea manifest → cele trei puncte → Fixează în partea de sus a paginii. Schimbi coperta paginii cu 08-coperta-facebook.png.',
        'Alternativ: îi dai sesiunii Claude de pe calculatorul tău promptul de mai jos și le programează ea, ca la postările din septembrie.']},
    {'etapa': 'TikTok (marți 6 oct, 20 min, apoi săptămânal)', 'pasi': [
        'Profil → Editează profilul: bio-ul de mai jos. Dacă profilul permite link, pui https://wa.me/40771311941.',
        'Clipurile: TikTok Studio pe calculator → Încarcă → descrierea + hashtagurile → Programează la 18:00. TikTok permite programarea cu până la 10 zile înainte.',
        'Postările foto (7 și 9 oct): din aplicație, + → Fotografii, alegi imaginile în ordine, adaugi un sunet din „Trending” și publici la 18:00.',
        'În fiecare clip din campanie: eticheta 07-video-eticheta.png pusă peste video în primele 3 secunde și cadrul final 06-video-final.png la sfârșit.',
        'TikTok Promote (13, 20 și 27 oct): pe clipul cu cel mai bun timp de vizionare din săptămâna trecută → Promovează → Obiectiv: vizite pe profil → Public personalizat: 25–54 de ani, locația cea mai apropiată de Botoșani pe care o oferă → 30 lei/zi, 3 zile.']},
    {'etapa': 'Verificare înainte de fiecare publicare', 'pasi': [
        'Mașina e încă în parc și prețul e cel de pe site.',
        'Un preț tăiat apare doar dacă prețul vechi a fost cel mai mic preț practicat în ultimele 30 de zile (regula ANPC pentru reduceri).',
        'La mașinile cu TVA deductibil, prețul final cu TVA e cel mai vizibil, iar „+ TVA” apare doar pentru firme.',
        'Numerele de înmatriculare și datele fostului proprietar din acte sunt acoperite.',
        'Clientul de la predare și-a dat acordul să apară; altfel filmezi doar mâinile și cheile.',
        'Numărul 0771 311 941 și linkul wa.me/40771311941 sunt corecte.',
        'Pe Tesla: FSD apare ca pachet cumpărat, cu funcții limitate în UE, nu ca „inclus” fără explicații.']},
    {'etapa': 'După lansare: rutina de luni (15 min)', 'pasi': [
        'Ads Manager → coloanele: Cheltuieli, Conversații prin mesagerie începute, Cost pe conversație, CTR (link).',
        'WhatsApp: numeri conversațiile cu eticheta DOSAR, test drive-urile programate și mașinile vândute din campanie.',
        'TikTok Studio → Analize: vizualizări, timp mediu de vizionare și comentarii pe clip.',
        'Regulă: o reclamă care a cheltuit peste 60 de lei cu un cost pe conversație de peste 25 de lei se oprește.',
        'Regulă: dacă tot setul are costul peste 25 de lei după 7 zile, schimbi întâi vizualul (V1 în loc de static), apoi publicul.',
        'Regulă: o mașină vândută iese din reclame în aceeași zi (altfel plătești mesaje pentru o mașină care nu mai există).',
        'Îmi trimiți cifrele și îți spun ce schimbăm pentru săptămâna următoare.']},
]

PROMPT_LOCAL = (
    'Deschide Meta Business Suite pentru pagina West-Auto Botoșani și programează postările Facebook din calendarul campaniei '
    '„Fără povești” pentru 7–16 octombrie 2026, la ora 19:00, folosind textele și imaginile din folderul '
    'campanie-fara-povesti (branch-ul claude/campanie-facebook-tiktok-4op4k2 din repo-ul serbanbtz/PC). '
    'Imaginile sunt în vizuale/, textele în 03-texte.md, calendarul în 05-calendar.md. '
    'Înainte de fiecare postare verifică pe site că mașina e încă de vânzare și că prețul e același; dacă nu, sari peste ea și spune-mi. '
    'Nu publica nimic imediat: doar programează. În Ads Manager creează campania „WA | Fără povești | oct 2026” exact după 06-lansare.md, '
    'dar las-o ca schiță: o public eu.')

data = dict(reclame=RECLAME, structura=STRUCTURA, buget=BUGET, postari=POSTARI, tiktok=TIKTOK, whatsapp=WHATSAPP,
            video=[dict(v, cadre=[dict(timp=a, ce=b, text=c) for a, b, c in v['cadre']]) for v in VIDEO],
            calendar=CALENDAR, pasi=PASI, prompt_local=PROMPT_LOCAL)
json.dump(data, open(os.path.join(ROOT, 'campanie.json'), 'w'), ensure_ascii=False, indent=1)

# ---------------------------------------------------------------- Documente .md generate
ZILE = ['Luni', 'Marți', 'Miercuri', 'Joi', 'Vineri', 'Sâmbătă', 'Duminică']
import datetime


def zi(d):
    t = datetime.date.fromisoformat(d)
    return f'{ZILE[t.weekday()]} {t.day} {"oct" if t.month == 10 else "nov"}'


def q(text):
    return '\n'.join('> ' + l if l else '>' for l in text.split('\n'))


md = ['# 03 · Texte gata de copiat', '',
      'Toate textele campaniei, în ordinea în care le folosești. Pe pagina campaniei au buton de copiere.', '',
      '## Reclame Meta (Facebook + Instagram)', '']
for t in RECLAME['texte_principale']:
    md += [f'### {t["id"]} · {t["nume"]}', '', q(t['text']), '']
md += ['### Titluri (câte unul pe reclamă)', ''] + [f'- {t}' for t in RECLAME['titluri']] + ['',
       f'**Descriere:** {RECLAME["descriere"]}', '', f'**Mesaj precompletat (setul A):** „{RECLAME["mesaj_precompletat_general"]}”', '',
       '### Reclamele cu dosar (setul B)', '']
for d in RECLAME['dosare']:
    md += [f'#### {d["nume"]} · `{d["vizual"]}`', '', q(d['text']), '', f'Mesaj precompletat: „{d["mesaj_precompletat"]}”', '']
md += ['## Postări Facebook', '']
for k, p in POSTARI.items():
    md += [f'### {k} · {p["nume"]}', '', f'Vizual: `{p["vizual"]}`', '', q(p['text']), '']
md += ['## TikTok', '', f'**Bio:** {TIKTOK["bio"]}', '', f'**Hashtaguri:** `{TIKTOK["hashtaguri"]}`', '', '| Clip | Descriere |', '|---|---|']
md += [f'| {k} | {v} |' for k, v in TIKTOK['descrieri'].items()]
md += ['', '## WhatsApp Business', '', '**Etichete:** ' + ' · '.join(WHATSAPP['etichete']), '',
       '**Mesaj de bun venit:**', '', q(WHATSAPP['salut']), '', '**Mesaj de absență:**', '', q(WHATSAPP['absent']), '',
       '**Răspunsuri rapide:**', '']
for r in WHATSAPP['rapide']:
    md += [f'- `{r["cod"]}`: {r["text"]}']
md += ['', '## Răspunsuri la comentarii', '', '| Când cineva scrie | Răspunsul |', '|---|---|']
md += [f'| {c["cand"]} | {c["raspuns"]} |' for c in WHATSAPP['comentarii']]
open(os.path.join(ROOT, '03-texte.md'), 'w').write('\n'.join(md) + '\n')

md = ['# 04 · Scripturi video', '', 'Toate clipurile sunt verticale (9:16), filmate cu telefonul după regulile din „Schema de filmare TikTok”. '
      'În fiecare clip al campaniei pui eticheta `07-video-eticheta.png` în primele 3 secunde și cadrul final `06-video-final.png` la sfârșit.', '']
for v in VIDEO:
    md += [f'## {v["id"]} · {v["titlu"]}', '', f'**Durată:** {v["durata"]} · **Rol:** {v["rol"]}', '', f'**Cine apare:** {v["cine"]}', '',
           '| Timp | Ce se vede | Text pe ecran |', '|---|---|---|']
    md += [f'| {a} | {b} | {c or "—"} |' for a, b, c in v['cadre']]
    md += ['', f'**Variantă:** {v["varianta"]}', '', f'**Sunet:** {v["sunet"]}', '']
open(os.path.join(ROOT, '04-scripturi-video.md'), 'w').write('\n'.join(md) + '\n')

md = ['# 05 · Calendarul campaniei (4 octombrie – 2 noiembrie 2026)', '',
      'TikTok la 18:00, Facebook la 19:00, ca în planul din octombrie. Codurile P1–P6 și D (dosar) trimit la textele din `03-texte.md`.', '']
faza = None
for c in CALENDAR:
    if c['faza'] != faza:
        faza = c['faza']
        md += ['', f'## Faza: {faza}', '', '| Zi | Facebook 19:00 | TikTok 18:00 | Reclame | Tu / echipa |', '|---|---|---|---|---|']
    md += [f'| {zi(c["data"])} | {c["facebook"] or "—"} | {c["tiktok"] or "—"} | {c["reclame"] or "—"} | {c["tu"] or "—"} |']
open(os.path.join(ROOT, '05-calendar.md'), 'w').write('\n'.join(md) + '\n')

md = ['# 06 · Lansare pas cu pas', '', 'Ordinea exactă în care se face totul, până la publicare. Durata e estimată pentru cineva care a mai folosit Business Suite.', '',
      '## Structura reclamelor Meta', '']
for s in STRUCTURA:
    md += [f'### {s["nivel"]}: {s["nume"]}' + (f' · {s["buget"]}' if s.get('buget') else ''), ''] + [f'- {x}' for x in s['setari']]
    if s.get('reclame'):
        md += ['', '**Reclame:**', ''] + [f'- {x}' for x in s['reclame']]
    md += ['']
md += ['## Bugetul', '', '| Variantă | Meta | TikTok | Total 7 oct – 1 nov | Când o alegi |', '|---|---|---|---|---|']
md += [f'| {b["varianta"]} | {b["meta"]} | {b["tiktok"]} | {b["total"]} | {b["cand"]} |' for b in BUGET]
md += ['']
for e in PASI:
    md += [f'## {e["etapa"]}', ''] + [f'- [ ] {p}' for p in e['pasi']] + ['']
md += ['## Prompt pentru sesiunea Claude de pe calculatorul tău', '', 'Dacă vrei ca programarea să o facă sesiunea Claude cu Chrome (ca la postările din septembrie), îi dai textul acesta:', '', q(PROMPT_LOCAL), '']
open(os.path.join(ROOT, '06-lansare.md'), 'w').write('\n'.join(md) + '\n')
print('ok:', len(CALENDAR), 'zile,', len(POSTARI), 'postări,', len(VIDEO), 'scripturi')
