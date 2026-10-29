# Carrousel LinkedIn vd_li_04 (29/10/2026) : 6 lignes qui font grimper la facture. Réutilise l'en-tête de render_semaine1.py.
import asyncio, os
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_semaine1.py")
src = open(SRC, encoding="utf-8").read().split("# ---------- LI-1")[0]
exec(src)
N = 6

def footer(n):
    return f"""<div style="position:absolute;left:88px;right:88px;bottom:72px;display:flex;justify-content:space-between;align-items:center">
<img src="{LOGO_H}" style="height:48px"><div style="font-weight:700;font-size:26px;color:rgba(0,48,70,.5)">{n} / {N}</div></div>"""

def line_card(num, tag, title, txt, where):
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
{line_card(*a)}{line_card(*b)}
</div>{footer(n)}""")

slides = []
slides.append(page(1080, 1350, "dark", f"""
<img class="fox" src="{FOX}" style="right:-220px;bottom:-160px;width:900px;opacity:.12">
<div style="padding:110px 88px 0">
  <div class="eyebrow" style="font-size:28px">Le vrai coût de vos contrats</div>
  <h1 style="margin-top:56px;font-weight:800;font-size:98px;line-height:1.03;letter-spacing:-.025em"><span class="or">6 lignes</span> de vos contrats fournisseurs qui font <span class="teal">grimper la facture</span>.</h1>
  <p style="margin-top:48px;font-weight:500;font-size:36px;line-height:1.4;color:rgba(0,48,70,.75);max-width:850px">Télécom, énergie, terminal de paiement, maintenance, leasing : le prix signé bouge souvent sans que personne ne le renégocie.</p>
</div>
<div style="position:absolute;left:88px;bottom:170px;font-weight:700;font-size:32px;color:{BLUE}">Faites défiler →</div>
{footer(1)}"""))

slides.append(pair(2,
  (1, "Indexation", "Le prix révisé chaque année", "Un indice ou un pourcentage fixé au contrat s'applique automatiquement, année après année.", "Cherchez « indexation », « révision » ou « indice »"),
  (2, "Frais annexes", "Les frais qui s'ajoutent au prix", "Location du terminal, frais de service, frais de dossier : ils ne figurent pas toujours dans le prix affiché.", "Comparez la grille tarifaire et votre dernière facture"),
  "light"))
slides.append(pair(3,
  (3, "Options reconduites", "L'option « offerte » qui ne l'est plus", "Une option ajoutée en cours de route peut devenir payante, puis se reconduire avec le contrat.", "Listez les options facturées, et celles que vous utilisez"),
  (4, "Engagement minimum", "Le volume ou la durée imposés", "Un minimum de commande ou de durée peut coûter cher si votre activité a changé.", "Repérez minimums, durée d'engagement et frais de sortie"),
  "dark"))
slides.append(pair(4,
  (5, "Fin de leasing", "Le loyer qui continue", "Selon les contrats, sans restitution ni courrier dans les formes, la location peut se prolonger.", "Notez la date de fin et les conditions de restitution"),
  (6, "Modification tarifaire", "La hausse annoncée par e-mail", "Une nouvelle grille peut s'appliquer après simple notification, avec souvent un délai pour la refuser.", "Relisez les conditions de modification du prix"),
  "light"))

rows = [("Prix signé (année 1)", "2 400 €", NAVY, False),
        ("Indexation 3 %/an, 2 ans", "+ 146 €", ORANGE, True),
        ("Option devenue payante (15 €/mois)", "+ 180 €", ORANGE, True),
        ("Frais de service annuels", "+ 120 €", ORANGE, True)]
rhtml = "".join(f"""<div style="display:flex;justify-content:space-between;align-items:center;padding:20px 0;border-bottom:2px solid rgba(0,48,70,.08)">
<span style="font-weight:600;font-size:34px">{l}</span><span style="font-weight:800;font-size:40px;color:{c};white-space:nowrap">{v}</span></div>""" for l, v, c, _ in rows)
slides.append(page(1080, 1350, "dark", f"""
<img class="fox" src="{FOX}" style="right:-200px;top:-120px;width:640px;opacity:.10">
<div style="padding:84px 88px 0">
  <div class="eyebrow" style="font-size:26px">Exemple illustratif</div>
  <h2 style="margin-top:36px;font-weight:800;font-size:74px;line-height:1.06;letter-spacing:-.02em">Un contrat de maintenance, <span class="teal">3 ans plus tard</span>.</h2>
  <div style="margin-top:40px;background:#fff;border-radius:28px;padding:14px 44px 26px;box-shadow:0 2px 0 rgba(0,48,70,.06)">
    {rhtml}
    <div style="display:flex;justify-content:space-between;align-items:center;padding-top:30px">
      <span style="font-weight:800;font-size:38px">Payé en année 3</span><span style="font-weight:800;font-size:58px;color:{NAVY};white-space:nowrap">2 846 €</span></div>
  </div>
  <p style="margin-top:34px;font-weight:700;font-size:38px;line-height:1.3">Soit <span class="or">+ 446 € par an</span> (+ 18,6 %), sans aucune renégociation.</p>
  <p style="margin-top:18px;font-weight:500;font-size:24px;color:rgba(0,48,70,.55)">Montants HT fictifs, pour illustrer le mécanisme.</p>
</div>{footer(5)}"""))

feat = ["Clauses clés de chaque contrat mises en avant", "Risques signalés et Score Volpi sur 100", "Échéances et préavis extraits automatiquement", "Garanties et services en doublon détectés"]
fhtml = "".join(f"""<li style="display:flex;gap:22px;align-items:center;margin-top:24px">
<span style="flex:none;width:40px;height:40px;border-radius:50%;background:{TEAL};color:{NAVY};font-weight:800;font-size:24px;display:flex;align-items:center;justify-content:center">✓</span><span>{f}</span></li>""" for f in feat)
slides.append(page(1080, 1350, "light", f"""
<img class="fox" src="{FOX}" style="right:-180px;top:-100px;width:700px;opacity:.12">
<div style="padding:110px 88px 0">
  <div class="eyebrow" style="font-size:26px">Votre copilote</div>
  <h2 style="margin-top:40px;font-weight:800;font-size:78px;line-height:1.06;letter-spacing:-.02em">Volpi ne décide pas à votre place. Il rend visible <span class="blue">ce que vous ne lisez pas</span>.</h2>
  <ul style="list-style:none;margin-top:40px;font-weight:700;font-size:34px;line-height:1.3">{fhtml}</ul>
  <div style="margin-top:56px;background:linear-gradient(120deg,{BLUE},{TEAL2});color:#fff;border-radius:28px;padding:36px 44px">
    <div style="font-weight:800;font-size:38px;line-height:1.25">Combien ces petites lignes vous coûtent&#8209;elles&nbsp;?</div>
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
