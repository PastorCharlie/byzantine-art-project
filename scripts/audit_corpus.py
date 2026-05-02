#!/usr/bin/env python3
"""
Audit script for the Byzantine Art Project corpus.

Applies #84.5 / #110-reconciliation bucketing conventions:
- workshop / tradition-type / icon-type entries tracked separately (not against museum 4-ceiling)
- manuscripts tracked separately (3-ceiling each)
- Sinai-origin entries housed elsewhere counted under current housing, not Sinai
- Cappella Palatina spelling variants ("Capella" / "Cappella") merged
- Hagia Eirene Istanbul has a dedicated case (added at #110 reconciliation)

Usage:
    python3 scripts/audit_corpus.py
"""
import json
import os
import collections


WORKSHOP_TRADITION_ICON_TYPE = {
    "saint-anthony-damaskenos",
    "saint-stephen-protomartyr",
    "saint-christopher-cynocephalus",
    "michael-weighing-souls",
    "three-hebrews-furnace",
    "theotokos-hodegetria",
    "john-damascus-tzanes",
    "lord-sabaoth-vresok-old-believer",
}

MANUSCRIPT_SLUGS = {
    "four-evangelists-rabbula",
    "rossano-gospels-healing-blind-man",
    "khludov-psalter-folio-67r",
    "nikephoros-khludov-psalter",
    "red-sea-khludov-psalter",
    "rebecca-vienna-genesis",
    "argument-icons-madrid-skylitzes",
    "leo-v-monk-madrid-skylitzes",
    "good-samaritan-rossano",
    "jacob-blessing-vienna-genesis",
    "pentecost-rabbula",
    "christ-pilate-rossano",
    "menologion-basil-second-nicaea",
    "john-prochorus-armenian",
    "gethsemane-walters-armenian",
    "joseph-vienna-genesis",
    "david-paris-psalter",
}

SINAI_ORIGIN_OTHER_HOUSING = {
    "sergius-bacchus-khanenko",
}


def bucket(slug, loc):
    loc = loc.lower()
    if slug in WORKSHOP_TRADITION_ICON_TYPE:
        return ("workshop-tradition-icontype", slug)
    if slug in MANUSCRIPT_SLUGS:
        return ("manuscript", slug)
    # Sinai-origin housed elsewhere
    if slug in SINAI_ORIGIN_OTHER_HOUSING:
        if "khanenko" in loc:
            return ("museum", "Khanenko Museum Kyiv")
    # Sites
    if "capella palatina" in loc or "cappella palatina" in loc or "palatine chapel" in loc:
        return ("site", "Cappella Palatina")
    if "hagia sophia" in loc and "thessalon" in loc:
        return ("site", "Hagia Sophia Thessaloniki")
    if "hagia sophia" in loc and "kyiv" in loc:
        return ("site", "Hagia Sophia Kyiv")
    if "hagia sophia" in loc and "ohrid" in loc:
        return ("site", "Hagia Sophia Ohrid")
    if "hagia sophia" in loc:
        return ("site", "Hagia Sophia Constantinople")
    if "hagia eirene" in loc or "saint irene" in loc or "haghia eirene" in loc:
        return ("site", "Hagia Eirene Constantinople")
    if "saint catherine" in loc or "st. catherine" in loc or "st catherine" in loc:
        return ("site", "Sinai (St Catherine)")
    if "hosios loukas" in loc:
        return ("site", "Hosios Loukas")
    if "daphni" in loc:
        return ("site", "Daphni")
    if "chora" in loc or "kariye" in loc:
        return ("site", "Chora")
    if "pammakaristos" in loc or "fethiye" in loc:
        return ("site", "Pammakaristos")
    if "hosios david" in loc or "latomos" in loc:
        return ("site", "Hosios David Thessaloniki")
    if "rotunda" in loc:
        return ("site", "Rotunda Thessaloniki")
    if "saint demetrios" in loc and "thessalon" in loc:
        return ("site", "Saint Demetrios Thessaloniki")
    if "thessalon" in loc:
        return ("site", "Thessaloniki (other)")
    if "cefalu" in loc or "cefalù" in loc:
        return ("site", "Cefalù")
    if "monreale" in loc:
        return ("site", "Monreale")
    if "martorana" in loc:
        return ("site", "Martorana")
    if "san vitale" in loc:
        return ("site", "San Vitale Ravenna")
    if "sant'apollinare nuovo" in loc or "santapollinare nuovo" in loc or "sant apollinare nuovo" in loc or "sant’apollinare nuovo" in loc:
        return ("site", "Sant'Apollinare Nuovo")
    if "classe" in loc:
        return ("site", "Sant'Apollinare in Classe")
    if "battistero degli ariani" in loc or "arian baptistery" in loc:
        return ("site", "Arian Baptistery Ravenna")
    if "torcello" in loc:
        return ("site", "Torcello")
    if "san marco" in loc:
        return ("site", "San Marco Venice")
    if "santi cosma" in loc:
        return ("site", "Santi Cosma e Damiano Rome")
    if "vatopedi" in loc:
        return ("site", "Vatopedi Athos")
    if "stavronikita" in loc:
        return ("site", "Stavronikita Athos")
    if "panagia tou arakou" in loc or "panagia arakos" in loc or "arakos" in loc:
        return ("site", "Panagia tou Arakou Cyprus")
    if "asinou" in loc:
        return ("site", "Asinou Cyprus")
    if "tokali" in loc or "tokal" in loc:
        return ("site", "Tokalı Kilise Cappadocia")
    if "karanl" in loc:
        return ("site", "Karanlık Kilise Cappadocia")
    if "carikli" in loc or "çarıklı" in loc or "arıklı" in loc:
        return ("site", "Çarıklı Kilise Cappadocia")
    if "voronet" in loc or "voroneț" in loc or "vorone" in loc:
        return ("site", "Voroneț")
    if "mileseva" in loc or "mileševa" in loc:
        return ("site", "Mileševa")
    if "decani" in loc or "dečani" in loc:
        return ("site", "Visoki Dečani")
    if "gracanica" in loc or "gračanica" in loc:
        return ("site", "Gračanica")
    if "nerezi" in loc:
        return ("site", "Nerezi")
    if "boyana" in loc:
        return ("site", "Boyana")
    if "tsalenjikha" in loc:
        return ("site", "Tsalenjikha")
    if "pantanassa" in loc:
        return ("site", "Mistra Pantanassa")
    if "kastoria" in loc:
        return ("site", "Kastoria")
    if "kurbinovo" in loc:
        return ("site", "Kurbinovo (Saint George)")
    if "agiasmati" in loc or "stavros tou agiasmati" in loc or "platanistasa" in loc:
        return ("site", "Stavros tou Agiasmati Cyprus")
    if "san bartolomeo" in loc and "armeni" in loc:
        return ("site", "San Bartolomeo degli Armeni Genoa")
    if "louvre" in loc:
        return ("museum", "Louvre Paris")
    if "peribleptos" in loc and ("mistra" in loc or "mystras" in loc):
        return ("site", "Mistra Peribleptos")
    if "spoleto" in loc:
        return ("site", "Spoleto Cathedral")
    if "sucevița" in loc or "sucevita" in loc:
        return ("site", "Sucevița Monastery")
    if "cozia" in loc:
        return ("site", "Cozia Monastery")
    if "catacomb of priscilla" in loc or "priscilla" in loc and "catacomb" in loc:
        return ("site", "Catacomb of Priscilla Rome")
    if "catacomb of saints marcellinus" in loc or "marcellinus" in loc:
        return ("site", "Catacomb of Marcellinus and Peter Rome")
    if "vatican apostolic library" in loc:
        return ("manuscript", "Vatican Library")
    if "andrey rublev museum" in loc or "andronikov" in loc:
        return ("museum", "Andrey Rublev Museum Moscow")
    if "saint sophia cathedral, ohrid" in loc or "ohrid" in loc:
        return ("site", "Saint Sophia Ohrid")
    if "sebaste" in loc or "forty martyrs" in loc:
        return ("site", "Sebaste")
    if "three hierarchs" in loc and "albania" in loc:
        return ("site", "Three Hierarchs Albania")
    if "bawit" in loc:
        return ("site", "Bawit Egypt")
    # Museums
    if "british museum" in loc:
        return ("museum", "British Museum London")
    if "metropolitan" in loc:
        return ("museum", "Met Museum NY")
    if "walters" in loc:
        return ("museum", "Walters Baltimore")
    if "hermitage" in loc:
        return ("museum", "Hermitage")
    if "russian museum" in loc or "русский музей" in loc:
        return ("museum", "Russian Museum St Petersburg")
    if "tretyakov" in loc or "tretiakov" in loc:
        return ("museum", "Tretyakov Moscow")
    if "khanenko" in loc:
        return ("museum", "Khanenko Museum Kyiv")
    if "bode" in loc:
        return ("museum", "Bode Berlin")
    if "dumbarton" in loc:
        return ("museum", "Dumbarton Oaks DC")
    if "vatican" in loc and "library" not in loc:
        return ("museum", "Vatican Museums")
    if "byzantine and christian museum" in loc and "athens" in loc:
        return ("museum", "Byzantine Museum Athens")
    if "coptic museum" in loc:
        return ("museum", "Coptic Museum Cairo")
    if "national museum of georgia" in loc or "shalva amiranashvili" in loc:
        return ("museum", "National Museum of Georgia")
    if "national historical museum" in loc and "tirana" in loc:
        return ("museum", "Tirana National Historical Museum")
    if "kyiv" in loc:
        return ("site", "Hagia Sophia Kyiv")
    return ("OTHER", loc[:60])


def main():
    base = "data/artworks"
    files = sorted(os.listdir(base))
    entries = []
    for f in files:
        with open(os.path.join(base, f)) as fp:
            entries.append((f, json.load(fp)))

    buckets = collections.defaultdict(list)
    for f, d in entries:
        cat, key = bucket(d["slug"], d.get("location_name", ""))
        buckets[(cat, key)].append(d["slug"])

    print(f"Total entries on disk: {len(entries)}")
    print()
    print("=== SITES (4-ceiling) ===")
    for (cat, key), slugs in sorted(buckets.items()):
        if cat == "site":
            flag = ""
            if len(slugs) >= 5:
                flag = "  *** OVER CEILING"
            elif len(slugs) == 4:
                flag = "  [at ceiling]"
            print(f"  {key}: {len(slugs)}{flag}")
    print()
    print("=== MUSEUMS (4-ceiling) ===")
    for (cat, key), slugs in sorted(buckets.items()):
        if cat == "museum":
            flag = ""
            if len(slugs) >= 5:
                flag = "  *** OVER CEILING"
            elif len(slugs) == 4:
                flag = "  [at ceiling]"
            print(f"  {key}: {len(slugs)}{flag}")
    print()
    print("=== MANUSCRIPTS (3-ceiling each) ===")
    print(f"  {sum(1 for (c, _), _ in buckets.items() if c == 'manuscript')} manuscript-tracked entries")
    print()
    print("=== WORKSHOP/TRADITION/ICON-TYPE ===")
    print(f"  {sum(1 for (c, _), _ in buckets.items() if c == 'workshop-tradition-icontype')} entries")
    print()
    other = [(k, slugs) for (cat, k), slugs in buckets.items() if cat == "OTHER"]
    if other:
        print("=== UNBUCKETED (script gap) ===")
        for k, slugs in other:
            for s in slugs:
                print(f"  - {s}: loc='{k}'")
    else:
        print("=== UNBUCKETED: none ===")


if __name__ == "__main__":
    main()
