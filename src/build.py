# -*- coding: utf-8 -*-
import csv, json, re, sys, unicodedata
import os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from data import ITEMS

OUT = sys.argv[1]
BASE = "https://choubz.github.io/activites-enfants-montreal/"

def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:60].strip("-")

seen = {}
for it in ITEMS:
    s = slug(it["nom"]) or "fiche"
    n = seen.get(s, 0) + 1
    seen[s] = n
    it["id"] = s if n == 1 else "%s-%d" % (s, n)

SRC = {"tt": "Activités (TikTok + sites officiels)", "web": "Ajouts web", "parc": "Parcs et plein air"}

def clean(v):
    return "" if v in (None, "n.d.") else v

# ---------------------------------------------------------------- carte.csv
rows = []
for it in ITEMS:
    for suffix, q, prec in it["markers"]:
        titre = it["nom"] + (" – " + suffix if suffix else "")
        parts = [it["typ"], it["age"], it["prix"], it["saison"]]
        desc = " · ".join(clean(p) for p in parts if clean(p))
        desc += " · Statut : " + it["statut"]
        if prec == "nom":
            desc += " · Repère placé d'après le nom du lieu : à vérifier sur la carte"
        rows.append([titre, q, prec, it["cat"], SRC[it["src"]], desc, BASE + "#" + it["id"]])

with open(OUT + "/carte.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Nom", "Recherche (adresse ou lieu)", "Précision", "Catégorie", "Section", "Description", "Fiche (lien)"])
    w.writerows(rows)

# ---------------------------------------------------------------- non placés
np_ = [it["nom"] for it in ITEMS if not it["markers"]]

# ---------------------------------------------------------------- index.html
payload = []
for it in ITEMS:
    payload.append(dict(id=it["id"], src=it["src"], cat=it["cat"], nom=it["nom"], typ=clean(it["typ"]), lieu=clean(it["lieu"]),
                        age=clean(it["age"]), prix=clean(it["prix"]), saison=clean(it["saison"]), liens=it["liens"],
                        compte=it["compte"] or "", statut=it["statut"], notes=it["notes"], free=it["free"], tags=it["tags"],
                        placed=bool(it["markers"]), q=(it["markers"][0][1] if it["markers"] else "")))

HTML = open(HERE + "/template.html", encoding="utf-8").read()
HTML = HTML.replace("__DATA__", json.dumps(payload, ensure_ascii=False))
HTML = HTML.replace("__SRC__", json.dumps(SRC, ensure_ascii=False))
open(OUT + "/index.html", "w", encoding="utf-8").write(HTML)

print("fiches:", len(ITEMS), "| repères:", len(rows), "| non placés:", len(np_))
for n in np_:
    print("  non placé:", n)
