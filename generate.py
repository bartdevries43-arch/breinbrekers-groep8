#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Breinbrekers voor groep 8 - print-klare vellen (eigen, originele puzzels).
Elk vel heeft een 'Naam:'-regel en 5 verschillende breinbrekers in een omkaderd
blok. Achterin een antwoordblad voor de leerkracht.

Draai:  python3 generate.py   ->  breinbrekers.html
"""
import html

# (categorie, vraag, antwoord)   antwoord "" = creatief / eigen antwoord
PUZZELS = [
    # Vel 1
    ("Rekenpuzzel", "Ik denk aan een getal. Ik doe het keer 3 en tel er 6 bij op. Ik krijg 30. Welk getal is het?", "8"),
    ("Maak de rij af", "Welke getallen horen erbij?  2 – 4 – 8 – 16 – ___ – ___", "32 en 64 (steeds keer 2)"),
    ("Logisch denken", "Een boer heeft 17 schapen. Alle schapen behalve 9 lopen weg. Hoeveel houdt hij er over?", "9 schapen"),
    ("Codewoord", "De letters zijn nu cijfers: A=1, B=2, C=3 … Welk woord is dit?  12 – 5 – 26 – 5 – 14", "LEZEN"),
    ("Denk en teken", "Teken iets dat kan rollen, maar geen wielen heeft.", ""),
    # Vel 2
    ("Verhaaltjessom", "3 appels kosten samen € 1,20. Hoeveel kosten 7 van dezelfde appels?", "€ 2,80 (1 appel = € 0,40)"),
    ("Maak de rij af", "Welke getallen horen erbij?  1 – 4 – 9 – 16 – ___ – ___", "25 en 36 (de kwadraten)"),
    ("Woordpuzzel", "Maak van deze letters één bestaand woord:  T – R – A – A – T – S", "STRAAT"),
    ("Logisch denken", "Twee vaders en twee zonen vangen samen precies 3 vissen, en ieder krijgt er één. Hoe kan dat?", "Het zijn opa, vader en zoon: samen 3 personen."),
    ("Creatief", "Verzin een gloednieuw dier. Teken het en geef het een naam.", ""),
    # Vel 3
    ("Rekenpuzzel", "Welk getal hoort op de plek van de ?  ? × 4 + 10 = 110", "25"),
    ("Maak de rij af", "Welke getallen horen erbij?  90 – 81 – 72 – 63 – ___ – ___", "54 en 45 (er gaat steeds 9 af)"),
    ("Kraken", "Maak met de getallen 1, 2, 3 en 4 het getal 25. Je mag ×, − en + gebruiken.", "4 × 3 × 2 + 1 = 25"),
    ("Raadsel", "Ik heb steden maar geen huizen, bergen maar geen bomen en water maar geen vissen. Wat ben ik?", "Een landkaart"),
    ("Denk en teken", "Een cirkel is niet alleen een bal. Teken 3 andere dingen die rond zijn.", ""),
    # Vel 4
    ("Logisch denken", "Kijk goed naar het patroon:  A2 – B4 – C6 – D8 – ___ .  Wat komt hierna?", "E10 (letter één verder, getal telkens +2)"),
    ("Rekenpuzzel", "Een baksteen weegt 1 kilo plus een halve baksteen. Hoeveel weegt de hele baksteen?", "2 kilo"),
    ("Verhaaltjessom", "Een bus rijdt 60 km per uur en moet 180 km rijden. Onderweg pauzeert hij 30 minuten. Hoe lang duurt de hele reis?", "3 uur en 30 minuten"),
    ("Woordsoort", "Welk woord is een zelfstandig naamwoord?  rennen – tafel – snel – groen", "tafel"),
    ("Creatief", "Er gebeurde iets vreemds in de klas: alle stoelen … Schrijf het verhaal verder.", ""),
    # Vel 5
    ("Maak de rij af", "Welke getallen horen erbij?  1 – 1 – 2 – 3 – 5 – 8 – ___ – ___", "13 en 21 (som van de twee vorige)"),
    ("Logisch denken", "Overmorgen is het zondag. Welke dag is het vandaag?", "Vrijdag"),
    ("Rekenpuzzel", "Een slak zit onderin een put van 10 meter. Overdag klimt hij 3 meter, 's nachts zakt hij 2 meter terug. Na hoeveel dagen is hij boven?", "Na 8 dagen"),
    ("Codewoord", "A=1, B=2, C=3 … Kraak deze twee woorden:  7-18-15-5-16   en   1-3-8-20", "GROEP ACHT"),
    ("Denk en teken", "Teken een huis onder water. Bedenk wie daar woont en schrijf er één zin bij.", ""),
]

PER_VEL = 5
TINTS = ["#fdfaf1", "#f1f8f3", "#fdf0f4", "#eff5fc", "#f6f2fc"]


def esc(s):
    return html.escape(str(s))


def render_vak(nr, puz):
    cat, vraag, antw = puz
    creatief = (antw == "")
    lijnen = '<div class="lijnen"><span></span><span></span></div>' if creatief else ""
    return (f'<div class="vak">'
            f'<span class="vaknr">{nr}</span>'
            f'<h3>{esc(cat)}</h3>'
            f'<div class="inh">{esc(vraag)}</div>{lijnen}</div>')


def render_vel(index, puzzels, startnr):
    tint = TINTS[index % len(TINTS)]
    vakken = "".join(render_vak(startnr + i, p) for i, p in enumerate(puzzels))
    return (f'<section class="vel" style="--tint:{tint}">'
            f'<h1>Breinbrekers</h1>'
            f'<div class="naam">Naam:<span></span></div>'
            f'<div class="bundel">{vakken}</div>'
            f'<div class="voet">Groep 8 · brein-krakers 🧠</div></section>')


def render_antwoorden():
    rijen = "".join(
        f'<li><span class="anr">{i}.</span> <span class="acat">{esc(p[0])}:</span> '
        f'{esc(p[2]) if p[2] else "eigen antwoord (creatief)"}</li>'
        for i, p in enumerate(PUZZELS, 1)
    )
    return (f'<section class="vel antwoordvel" style="--tint:#ffffff">'
            f'<h1>Antwoorden</h1><ol class="antwoorden">{rijen}</ol></section>')


def vel_groepen():
    """Verdeel de puzzels in vellen; geef (index, puzzels, startnr) terug."""
    for v, i in enumerate(range(0, len(PUZZELS), PER_VEL)):
        yield v, PUZZELS[i:i + PER_VEL], i + 1


def htmldoc(titel, inner, printknop=True):
    btn = ('<button class="printknop" onclick="window.print()">🖨 Print deze pagina</button>'
           if printknop else "")
    return f'''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(titel)}</title>
<style>{CSS}</style>
</head>
<body>{btn}
{inner}
</body>
</html>'''


def bouw_alles():
    secties = [render_vel(v, p, s) for v, p, s in vel_groepen()]
    secties.append(render_antwoorden())
    return htmldoc("Breinbrekers · alle vellen", "".join(secties))


def bouw_vel_pagina(v, puzzels, startnr):
    return htmldoc(f"Breinbrekers · vel {v + 1}", render_vel(v, puzzels, startnr))


def bouw_antwoorden_pagina():
    return htmldoc("Breinbrekers · antwoordblad", render_antwoorden())


def bouw_index():
    kaartjes = []
    for v, puzzels, _ in vel_groepen():
        cats = " · ".join(dict.fromkeys(p[0] for p in puzzels))
        kaartjes.append(
            f'<a class="link vel-link" href="vel-{v + 1}.html">'
            f'<span class="lnr">Vel {v + 1}</span>'
            f'<span class="lcats">{esc(cats)}</span>'
            f'<span class="lprint">🖨 openen &amp; printen</span></a>')
    links = "".join(kaartjes)
    return f'''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Breinbrekers · groep 8</title>
<style>{INDEX_CSS}</style>
</head>
<body>
<div class="hero">
  <h1>🧠 Breinbrekers</h1>
  <p class="sub">Groep 8 · print-klare vellen</p>
  <p class="intro">Klik op een vel om het te openen en te printen (of gebruik de knop
  "Print deze pagina"). Kies bij het printen A4, marges "geen"/"standaard" en zet
  "achtergrondafbeeldingen" aan voor de kleuren.</p>

  <a class="link groot" href="breinbrekers.html">📄 Alle vellen + antwoordblad in één keer</a>

  <div class="grid">{links}</div>

  <a class="link antw" href="antwoorden.html">✅ Antwoordblad (voor de leerkracht)</a>
</div>
</body>
</html>'''


INDEX_CSS = """
*{margin:0;padding:0;box-sizing:border-box;}
body{font-family:"Trebuchet MS","Segoe UI",Verdana,sans-serif; color:#20272e; min-height:100vh;
  display:flex; align-items:center; justify-content:center; padding:26px;
  background:linear-gradient(135deg,#fdfaf1,#f1f8f3,#f6f2fc);}
.hero{background:#fff; border-radius:22px; box-shadow:0 10px 40px rgba(0,0,0,.12); padding:34px 30px;
  max-width:600px; width:100%; text-align:center;}
h1{font-family:Georgia,serif; font-size:40px; letter-spacing:2px; margin-bottom:2px;}
.sub{color:#2f7d4f; font-weight:bold; text-transform:uppercase; letter-spacing:2px; font-size:13px; margin-bottom:14px;}
.intro{color:#6b7680; font-size:14px; line-height:1.5; margin:0 auto 22px; max-width:460px;}
.link{display:block; text-decoration:none; border-radius:14px; padding:16px 18px; font-weight:bold; transition:transform .08s;}
.link:hover{transform:translateY(-2px);}
.groot{background:#2c5f8a; color:#fff; font-size:17px; margin-bottom:18px;}
.antw{background:#eaf3ee; color:#2f7d4f; margin-top:18px;}
.grid{display:grid; grid-template-columns:1fr 1fr; gap:12px;}
.vel-link{background:#f5f2fb; color:#4a3d70; text-align:left; display:flex; flex-direction:column; gap:3px;}
.lnr{font-size:17px;}
.lcats{font-weight:normal; font-size:11.5px; color:#7c8088; line-height:1.3;}
.lprint{font-weight:normal; font-size:12px; color:#8d6be8; margin-top:4px;}
@media(max-width:480px){ .grid{grid-template-columns:1fr;} }
"""


CSS = """
*{margin:0; padding:0; box-sizing:border-box;}
body{background:#e7e9ec; font-family:"Trebuchet MS","Segoe UI",Verdana,sans-serif; color:#20272e;}
.schermbalk{max-width:190mm; margin:16px auto; padding:12px 16px; background:#fff; border-radius:10px;
  font-size:13px; color:#444; box-shadow:0 1px 6px rgba(0,0,0,.12);}

.vel{width:210mm; min-height:297mm; margin:0 auto; background:var(--tint); padding:15mm 16mm;
  display:flex; flex-direction:column;}
h1{font-family:Georgia,"Times New Roman",serif; font-weight:700; text-transform:uppercase;
  letter-spacing:6px; text-align:center; font-size:40px; margin-bottom:10px;}
.naam{font-size:16px; display:flex; align-items:flex-end; gap:8px; margin-bottom:12px;}
.naam span{flex:1; border-bottom:2px solid #2b2b2b; height:16px;}

.bundel{flex:1; border:2.5px solid #2b2b2b; border-radius:6px; overflow:hidden; display:flex; flex-direction:column;}
.vak{flex:1; border-bottom:2px solid #2b2b2b; padding:12px 18px; display:flex; flex-direction:column;
  justify-content:center; position:relative; background:rgba(255,255,255,.45);}
.vak:last-child{border-bottom:none;}
.vaknr{position:absolute; top:8px; left:10px; font-size:12px; color:#9aa1a8; font-weight:bold;}
.vak h3{text-align:center; font-size:17px; font-weight:bold; margin-bottom:7px; color:#1a2027;}
.vak .inh{text-align:center; font-size:18px; line-height:1.42;}
.lijnen{margin-top:10px; display:flex; flex-direction:column; gap:12px;}
.lijnen span{border-bottom:1.5px dotted #9aa1a8; height:1px;}
.voet{text-align:center; color:#8a929a; font-size:12px; margin-top:10px;}

.antwoordvel h1{letter-spacing:4px;}
.antwoorden{list-style:none; display:flex; flex-direction:column; gap:5px; margin-top:4px;}
.antwoorden li{font-size:14px; line-height:1.35; border-bottom:1px dotted #cfd6db; padding-bottom:5px;}
.anr{font-weight:bold; color:#2c5f8a;}
.acat{font-weight:bold; color:#6b7680;}

@media print{
  body{background:#fff;}
  .schermbalk{display:none;}
  .vel{margin:0; min-height:auto; height:297mm; page-break-after:always;}
  .vak,.vel{-webkit-print-color-adjust:exact; print-color-adjust:exact;}
  @page{size:A4 portrait; margin:0;}
}
@media screen{ .vel{box-shadow:0 2px 14px rgba(0,0,0,.14); margin:16px auto;} }
.printknop{position:fixed; top:14px; right:14px; z-index:50; border:none; cursor:pointer;
  background:#2c5f8a; color:#fff; font-family:"Trebuchet MS",sans-serif; font-weight:bold;
  font-size:15px; padding:12px 18px; border-radius:12px; box-shadow:0 4px 14px rgba(0,0,0,.2);}
@media print{ .printknop{display:none;} }
"""


def schrijf(naam, inhoud):
    with open(naam, "w", encoding="utf-8") as f:
        f.write(inhoud)


def main():
    schrijf("index.html", bouw_index())
    schrijf("breinbrekers.html", bouw_alles())
    schrijf("antwoorden.html", bouw_antwoorden_pagina())
    for v, puzzels, startnr in vel_groepen():
        schrijf(f"vel-{v + 1}.html", bouw_vel_pagina(v, puzzels, startnr))
    vellen = (len(PUZZELS) + PER_VEL - 1) // PER_VEL
    print(f"Klaar: {len(PUZZELS)} breinbrekers op {vellen} vellen + antwoordblad.")
    print("  - index.html (startpagina met printbare links)")
    print(f"  - breinbrekers.html, antwoorden.html, vel-1..{vellen}.html")


if __name__ == "__main__":
    main()
