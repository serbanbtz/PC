// ============================================================
//  Aici modifici site-ul. Nu e nevoie să atingi index.html.
//  1. Completează datele firmei.
//  2. Pentru fiecare mașină din stoc, copiază un bloc { ... } și schimbă valorile.
//     Poza: pune fișierul în folderul "poze" și scrie aici numele lui.
//     Mașinile marcate exemplu: true apar cu eticheta EXEMPLU. Șterge-le când pui stocul real.
// ============================================================

window.FIRMA = {
  nume: "West Auto",
  slogan: "Mașini electrice și hibride second-hand, verificate și cu actele rezolvate.",
  telefon: "",            // ex. "0740 123 456"
  email: "",              // ex. "contact@westauto.ro"
  adresa: "",             // ex. "Str. Exemplu 10, Iași"
  program: "Luni–Vineri 9–18, Sâmbătă 10–14",
  facebook: "",           // link complet către pagina de Facebook
  autovit: "",            // link complet către pagina firmei de pe Autovit
  aniPePiata: null,       // ex. 8 (lasă null ca să nu apară)
};

window.STOC = [
  {
    exemplu: true,
    marca: "Tesla", model: "Model 3", versiune: "Long Range AWD",
    an: 2021, km: 68000, combustibil: "Electric", putere: 440,
    baterieSoH: 91, autonomie: 580,
    pret: 25900, tva: "marja",          // "marja" sau "deductibil"
    poza: "",                           // ex. "model3-alb.jpg"
    anunt: "",                          // link către anunțul de pe Autovit, dacă există
    dotari: ["Autopilot", "Pompă de căldură", "Plafon panoramic"],
  },
  {
    exemplu: true,
    marca: "Tesla", model: "Model Y", versiune: "Long Range AWD",
    an: 2022, km: 54000, combustibil: "Electric", putere: 514,
    baterieSoH: 93, autonomie: 533,
    pret: 31500, tva: "marja",
    poza: "", anunt: "",
    dotari: ["Autopilot", "Cârlig de remorcare", "Roți de iarnă"],
  },
  {
    exemplu: true,
    marca: "Toyota", model: "RAV4", versiune: "Hybrid AWD-i",
    an: 2020, km: 89000, combustibil: "Hibrid", putere: 222,
    pret: 24900, tva: "deductibil",
    poza: "", anunt: "",
    dotari: ["Cameră 360°", "Scaune încălzite", "Navigație"],
  },
];
