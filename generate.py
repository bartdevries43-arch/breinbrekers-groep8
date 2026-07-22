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


def bouw_document():
    vellen = []
    for v, i in enumerate(range(0, len(PUZZELS), PER_VEL)):
        vellen.append(render_vel(v, PUZZELS[i:i + PER_VEL], i + 1))
    vellen.append(render_antwoorden())
    return f'''<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Breinbrekers · groep 8</title>
<style>{CSS}</style>
</head>
<body>
<div class="schermbalk">Tip: druk op Ctrl/Cmd + P om te printen (A4, marges
"geen"/"standaard", "achtergrondafbeeldingen" aan voor de kleuren). Elk vel is één
A4. De laatste pagina is het antwoordblad voor de leerkracht.</div>
{"".join(vellen)}
</body>
</html>'''


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
"""


def main():
    with open("breinbrekers.html", "w", encoding="utf-8") as f:
        f.write(bouw_document())
    vellen = (len(PUZZELS) + PER_VEL - 1) // PER_VEL
    print(f"Klaar: {len(PUZZELS)} breinbrekers op {vellen} vellen + antwoordblad.")


if __name__ == "__main__":
    main()
