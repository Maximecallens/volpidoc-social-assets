"""Prépare un texte pour l'API LinkedIn (format « little text »).

LinkedIn tronque ou rejette le texte d'un post quand certains caractères
réservés ne sont pas échappés (le module Make ne le fait pas) :
    \\ | { } @ [ ] ( ) < > # * _ ~
Les hashtags (#Mot) sont convertis au format {hashtag|\\#|Mot} pour rester cliquables.

Usage :
    python3 tools/li_text.py posts/<dossier>/linkedin.txt          # texte échappé
    python3 tools/li_text.py posts/<dossier>/linkedin.txt --json   # chaîne JSON (carrousel)
"""
import json
import re
import sys

RESERVED = set("\\|{}@[]()<>#*_~")
HASHTAG = re.compile(r"(?<![\w&])#([0-9A-Za-zÀ-ÖØ-öø-ÿ_]+)")


def escape(text: str) -> str:
    out = []
    pos = 0
    for m in HASHTAG.finditer(text):
        out.append(_esc(text[pos:m.start()]))
        out.append("{hashtag|\\#|" + m.group(1).replace("_", "\\_") + "}")
        pos = m.end()
    out.append(_esc(text[pos:]))
    return "".join(out)


def _esc(s: str) -> str:
    return "".join("\\" + c if c in RESERVED else c for c in s)


if __name__ == "__main__":
    raw = open(sys.argv[1], encoding="utf-8").read().strip()
    res = escape(raw)
    print(json.dumps(res, ensure_ascii=False) if "--json" in sys.argv else res)
