# Carrousel LinkedIn vd_li_07 (12/11/2026) : perte d'exploitation, 6 questions à poser à votre multirisque. Réutilise l'en-tête de render_semaine1.py.
import asyncio, os
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_semaine1.py")
src = open(SRC, encoding="utf-8").read().split("# ---------- LI-1")[0]
exec(src)
N = 6

def footer(n):
    return f"""<div style="position:absolute;left:88px;right:88px;bottom:72px;display:flex;justify-content:space-between;align-items:center">
<img src="{LOGO_H}" style="height:48px"><div style="font-weight:700;font-size:26px;color:rgba(0,48,70,.5)">{n} / {N}</div></div>"""

def step_card(num, tag, title, txt, where):
    return f"""<div style="background:#fff;border-radius:28px;padding:36px 42px 38px;box-shadow:0 2px 0 rgba(0,48,70,.06)">
  <div style="display:flex;align-items:baseline;gap:22px">
    <div style="font-weight:800;font-size:86px;line-height:.9;color:{ORANGE}">0{num}</div>
    <div class="eyebrow" style="font-size:22px;color:{TEAL2}">{tag}</div>
  </div>
  <div style="margin-top:22px;font-weight:800;font-size:46px;line-height:1.12;letter-spacing:-.01em">{title}</div>
  <div style="margin-top:16px;font-weight:500;font-size:30px;line-height:1.38;color:rgba(0,48,70,.78)">{txt}</div>
  <div style="margin-top:20px;display:flex;gap:16px;align-items:flex-start;font-weight:700;font-size:26px;line-height:1.3;color:{BLUE}">
    <span style="flex:none;margin-top:2px;width:28px;height:28px;border-radius:8px;border:3px solid {TEAL}"></span><span>{where}</span></div>
</div>"""

def pair(n, a, b, cls):
    return page(1080, 1350, cls, f"""
<img class="fox" src="{FOX}" style="right:-200px;top:-120px;width:640px;opacity:.10">
<div style="position:absolute;inset:88px 88px 160px;display:flex;flex-direction:column;gap:34px;justify-content:center">
{step_card(*a)}{step_card(*b)}
</div>{footer(n)}""")

slides = []
slides.append(page(1080, 1350, "dark", f"""
<img class="fox" src="{FOX}" style="right:-220px;bottom:-160px;width:900px;opacity:.12">
<div style="padding:110px 88px 0">
  <div class="eyebrow" style="font-size:28px">Assurance · lire entre les lignes</div>
  <h1 style="margin-top:56px;font-weight:800;font-size:92px;line-height:1.04;letter-spacing:-.025em">Perte d'exploitation&nbsp;: <span class="or">6 questions</span> à poser à votre <span class="teal">multirisque</span>.</h1>
  <p style="margin-top:48px;font-weight:500;font-size:36px;line-height:1.4;color:rgba(0,48,70,.75);max-width:860px">Les murs sont réparés. Mais qui paie les semaines sans chiffre d'affaires&nbsp;? À vérifier avant le sinistre, pas après.</p>
</div>
<div style="position:absolute;left:88px;bottom:170px;font-weight:700;font-size:32px;color:{BLUE}">Faites défiler →</div>
{footer(1)}"""))

slides.append(pair(2,
  (1, "Présence", "La garantie est-elle souscrite&nbsp;?", "Elle est souvent proposée en option. Ce qui compte, c'est ce qui figure dans vos conditions particulières, pas dans la plaquette.", "Cherchez « perte d'exploitation » dans vos conditions particulières"),
  (2, "Déclencheurs", "Quels événements la déclenchent&nbsp;?", "Incendie, dégât des eaux, bris de machine… La liste varie d'un contrat à l'autre, et certaines causes peuvent être exclues.", "Comparez la liste à vos vrais risques&nbsp;: chambre froide, four, vitrine"),
  "light"))
slides.append(pair(3,
  (3, "Durée", "Combien de temps êtes-vous indemnisé&nbsp;?", "La période d'indemnisation est limitée, par exemple 3, 6 ou 12 mois. Retrouver sa clientèle prend parfois plus longtemps que les travaux.", "Notez la durée maximale prévue au contrat"),
  (4, "Franchise", "À partir de quel jour&nbsp;?", "La franchise est souvent exprimée en jours&nbsp;: les premiers jours de fermeture peuvent rester à votre charge.", "Notez le nombre de jours de franchise et le plafond"),
  "dark"))
slides.append(pair(4,
  (5, "Calcul", "Sur quelle base l'indemnité est-elle calculée&nbsp;?", "Marge brute, chiffre d'affaires, frais fixes&nbsp;: la base change tout. Et il faudra la justifier avec vos comptes.", "Gardez à portée de main les chiffres du dernier exercice"),
  (6, "Fournisseurs", "Et si c'est votre fournisseur qui s'arrête&nbsp;?", "La carence d'un fournisseur ou d'un client clé n'est pas toujours incluse, ou l'est avec des limites.", "Listez les fournisseurs sans lesquels vous fermez"),
  "light"))

rows = [("Garantie non souscrite", "0 €", ORANGE),
        ("Souscrite, franchise de 3 jours, plafond suffisant", "18 000 €", TEAL2),
        ("Souscrite, mais plafonnée à 10 000 €", "10 000 €", BLUE)]
rhtml = "".join(f"""<div style="display:flex;justify-content:space-between;align-items:center;gap:20px;padding:22px 0;border-bottom:2px solid rgba(0,48,70,.08)">
<span style="display:flex;gap:18px;align-items:center"><span style="flex:none;width:14px;height:54px;border-radius:7px;background:{c}"></span><span style="font-weight:600;font-size:31px;line-height:1.25">{l}</span></span><span style="font-weight:800;font-size:42px;color:{NAVY};white-space:nowrap">{v}</span></div>""" for l, v, c in rows)
slides.append(page(1080, 1350, "dark", f"""
<img class="fox" src="{FOX}" style="right:-200px;top:-120px;width:640px;opacity:.10">
<div style="padding:84px 88px 0">
  <div class="eyebrow" style="font-size:26px">Exemple illustratif</div>
  <h2 style="margin-top:36px;font-weight:800;font-size:68px;line-height:1.06;letter-spacing:-.02em">Un restaurant fermé <span class="or">3 semaines</span>. Trois contrats, trois issues.</h2>
  <p style="margin-top:28px;font-weight:600;font-size:30px;line-height:1.35;color:rgba(0,48,70,.78)">21 jours × 1 000 € de marge brute par jour = <b style="color:{NAVY}">21 000 € de perte</b>.</p>
  <div style="margin-top:34px;background:#fff;border-radius:28px;padding:14px 44px 22px;box-shadow:0 2px 0 rgba(0,48,70,.06)">
    <div style="font-weight:700;font-size:24px;color:rgba(0,48,70,.55);padding-top:14px;text-align:right">indemnité perte d'exploitation</div>
    {rhtml}
  </div>
  <p style="margin-top:34px;font-weight:700;font-size:34px;line-height:1.3">Même sinistre, même restaurant&nbsp;: <span class="or">c'est le contrat qui fait la différence</span>.</p>
  <p style="margin-top:18px;font-weight:500;font-size:24px;color:rgba(0,48,70,.55)">Montants fictifs et simplifiés, pour illustrer le mécanisme. Chaque contrat a ses propres règles.</p>
</div>{footer(5)}"""))

feat = ["Clauses clés de chaque contrat importé, extraites en clair", "Audit IA de couverture construit à partir de votre SIREN", "Garanties en doublon repérées", "Score Volpi sur 100 pour chaque contrat"]
fhtml = "".join(f"""<li style="display:flex;gap:22px;align-items:center;margin-top:24px">
<span style="flex:none;width:40px;height:40px;border-radius:50%;background:{TEAL};color:{NAVY};font-weight:800;font-size:24px;display:flex;align-items:center;justify-content:center">✓</span><span>{f}</span></li>""" for f in feat)
slides.append(page(1080, 1350, "light", f"""
<img class="fox" src="{FOX}" style="right:-180px;top:-100px;width:700px;opacity:.12">
<div style="padding:110px 88px 0">
  <div class="eyebrow" style="font-size:26px">Votre copilote</div>
  <h2 style="margin-top:40px;font-weight:800;font-size:78px;line-height:1.06;letter-spacing:-.02em">Volpi ne décide pas à votre place. Il rend visible <span class="blue">ce que vous ne lisez pas</span>.</h2>
  <ul style="list-style:none;margin-top:40px;font-weight:700;font-size:33px;line-height:1.3">{fhtml}</ul>
  <div style="margin-top:56px;background:linear-gradient(120deg,{BLUE},{TEAL2});color:#fff;border-radius:28px;padding:36px 44px">
    <div style="font-weight:800;font-size:38px;line-height:1.25">Combien vos contrats mal lus vous coûtent&#8209;ils&nbsp;?</div>
    <div style="margin-top:12px;font-weight:700;font-size:30px;color:#fff;opacity:.92">volpidoc.com/calculateur-roi</div>
  </div>
  <p style="margin-top:28px;font-weight:500;font-size:22px;color:rgba(0,48,70,.55)">Volpidoc est une aide à la lecture : ni courtier, ni conseil juridique.</p>
</div>{footer(6)}"""))

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for i, html in enumerate(slides, start=1):
            pg = await b.new_page(viewport={"width": 1080, "height": 1350})
            await pg.set_content(html)
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=f"{OUT}/li2-slide-{i}.png")
            await pg.close()
        await b.close()
asyncio.run(main())
print("ok")
