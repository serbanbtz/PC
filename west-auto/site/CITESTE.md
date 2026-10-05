# Site-ul West Auto: cum îl folosești

Site-ul are o singură pagină, care merge pe telefon și pe calculator. Nu ai nevoie de programator ca să-l actualizezi.

## Ce modifici
Totul se schimbă din fișierul **`stoc.js`**:
1. **Datele firmei:** telefon, adresă, e-mail, program, link-uri către Facebook și Autovit. Câmpurile lăsate goale nu apar pe site.
2. **Stocul:** fiecare mașină e un bloc `{ ... }`. Ca să adaugi o mașină, copiezi un bloc și schimbi valorile. Ca să o scoți după vânzare, ștergi blocul.
3. **Pozele:** pui fișierul (de exemplu `model3-alb.jpg`) în folderul `poze/` și scrii numele lui la `poza:`. Cel mai bine arată pozele pe orizontală.
4. **Exemplele:** cele trei mașini de acum au eticheta EXEMPLU. **Șterge-le** înainte să publici site-ul.

Deschide `index.html` în browser ca să vezi cum arată, înainte să-l pui online.

## Verifică textele
Textele de pe site (verificarea bateriei, telefonul după vânzare, finanțare, mașina la schimb) descriu ce face de obicei un dealer ca West Auto. **Păstrează doar ce faceți cu adevărat** și șterge restul din `index.html`.

## Cum îl pui online, gratuit
**Varianta cea mai simplă: Netlify Drop**
1. Intră pe app.netlify.com/drop.
2. Trage tot folderul `site` în pagină.
3. Primești pe loc un link. Îți faci cont gratuit ca să-l păstrezi și să legi un domeniu, de exemplu westauto.ro.

**Varianta GitHub Pages**
1. Faci un repository nou pe GitHub, de exemplu `westauto-site`, și urci în el conținutul folderului `site`.
2. Din Settings → Pages alegi branch-ul `main` și folderul `/ (root)`.
3. Site-ul apare în câteva minute la `numele-tau.github.io/westauto-site`.

La fiecare actualizare a stocului, urci din nou `stoc.js` (și pozele noi).
