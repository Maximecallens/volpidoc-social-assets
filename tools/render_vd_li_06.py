# Carrousel LinkedIn vd_li_06 (05/11/2026) : logiciels et abonnements SaaS, l'inventaire en 5 étapes. Réutilise l'en-tête de render_semaine1.py.
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
  <div class="eyebrow" style="font-size:28px">Reprendre la main</div>
  <h1 style="margin-top:56px;font-weight:800;font-size:96px;line-height:1.03;letter-spacing:-.025em">Logiciels et abonnements&nbsp;: <span class="or">l'inventaire</span> en <span class="teal">5 étapes</span>.</h1>
  <p style="margin-top:48px;font-weight:500;font-size:36px;line-height:1.4;color:rgba(0,48,70,.75);max-width:860px">Licences reconduites, comptes inactifs, outils en double&nbsp;: la méthode pour savoir ce que le cabinet paie vraiment, sans aucun outil.</p>
</div>
<div style="position:absolute;left:88px;bottom:170px;font-weight:700;font-size:32px;color:{BLUE}">Faites défiler →</div>
{footer(1)}"""))

slides.append(pair(2,
  (1, "Lister", "Tous les prélèvements récurrents", "Relevés bancaires et carte du cabinet sur 12 mois&nbsp;: les outils pris « pour tester » sont souvent payés par carte.", "Une ligne par outil, avec le montant réel prélevé"),
  (2, "Rattacher", "Les conditions de chaque abonnement", "Mensuel ou annuel, date de renouvellement, engagement, préavis&nbsp;: tout est dans les conditions acceptées à la souscription.", "Notez la prochaine date de renouvellement"),
  "light"))
slides.append(pair(3,
  (3, "Compter", "Licences payées / utilisateurs actifs", "Anciens collaborateurs, freelances de mission, comptes de test&nbsp;: un siège payé n'est pas un siège utilisé.", "Vérifiez la dernière connexion de chaque compte"),
  (4, "Regrouper", "Les outils qui font la même chose", "Deux outils de visio, trois espaces de stockage, deux solutions de signature&nbsp;: chacun choisi par quelqu'un de différent.", "Classez par usage, pas par éditeur"),
  "dark"))

choices = [("Garder", "l'outil sert, au bon nombre de licences", TEAL), ("Réduire", "retirer les sièges inactifs", BLUE), ("Résilier", "doublon ou outil oublié", ORANGE), ("Passer en annuel", "seulement pour un outil sûr", TEAL2)]
chtml = "".join(f"""<div style="display:flex;gap:22px;align-items:center;padding:20px 0;border-bottom:2px solid rgba(0,48,70,.08)">
<span style="flex:none;width:18px;height:58px;border-radius:9px;background:{c}"></span>
<span style="font-weight:800;font-size:38px;white-space:nowrap">{a}</span><span style="font-weight:500;font-size:28px;color:rgba(0,48,70,.7)">{b}</span></div>""" for a, b, c in choices)
slides.append(page(1080, 1350, "light", f"""
<img class="fox" src="{FOX}" style="right:-200px;top:-120px;width:640px;opacity:.10">
<div style="padding:96px 88px 0">
  <div style="display:flex;align-items:baseline;gap:22px">
    <div style="font-weight:800;font-size:86px;line-height:.9;color:{ORANGE}">05</div>
    <div class="eyebrow" style="font-size:22px;color:{TEAL2}">Décider</div>
  </div>
  <h2 style="margin-top:30px;font-weight:800;font-size:66px;line-height:1.08;letter-spacing:-.02em">Une décision par outil, <span class="teal">avant</span> la date de renouvellement.</h2>
  <div style="margin-top:40px;background:#fff;border-radius:28px;padding:10px 44px 22px;box-shadow:0 2px 0 rgba(0,48,70,.06)">{chtml}</div>
  <div style="margin-top:36px;display:flex;gap:16px;align-items:flex-start;font-weight:700;font-size:30px;line-height:1.35;color:{BLUE}">
    <span style="flex:none;margin-top:4px;width:30px;height:30px;border-radius:8px;border:3px solid {TEAL}"></span><span>Inscrivez dans votre agenda la date limite pour agir, préavis compris.</span></div>
</div>{footer(4)}"""))

rows = [("Suite bureautique : 9 licences, 6 utilisées", "540 €"),
        ("CRM : 5 sièges, 3 actifs", "720 €"),
        ("Visio : 2 outils pour le même usage", "240 €"),
        ("Signature : testée, jamais résiliée", "300 €")]
rhtml = "".join(f"""<div style="display:flex;justify-content:space-between;align-items:center;gap:20px;padding:20px 0;border-bottom:2px solid rgba(0,48,70,.08)">
<span style="font-weight:600;font-size:31px;line-height:1.25">{l}</span><span style="font-weight:800;font-size:40px;color:{ORANGE};white-space:nowrap">{v}</span></div>""" for l, v in rows)
slides.append(page(1080, 1350, "dark", f"""
<img class="fox" src="{FOX}" style="right:-200px;top:-120px;width:640px;opacity:.10">
<div style="padding:84px 88px 0">
  <div class="eyebrow" style="font-size:26px">Exemple illustratif</div>
  <h2 style="margin-top:36px;font-weight:800;font-size:72px;line-height:1.06;letter-spacing:-.02em">Un cabinet de 6 personnes, <span class="teal">une heure d'inventaire</span>.</h2>
  <div style="margin-top:40px;background:#fff;border-radius:28px;padding:14px 44px 26px;box-shadow:0 2px 0 rgba(0,48,70,.06)">
    <div style="font-weight:700;font-size:24px;color:rgba(0,48,70,.55);padding-top:14px;text-align:right">payé pour rien, par an</div>
    {rhtml}
    <div style="display:flex;justify-content:space-between;align-items:center;padding-top:30px">
      <span style="font-weight:800;font-size:38px">Total</span><span style="font-weight:800;font-size:58px;color:{NAVY};white-space:nowrap">1 800 €</span></div>
  </div>
  <p style="margin-top:34px;font-weight:700;font-size:36px;line-height:1.3">Soit <span class="or">150 € par mois</span> pour des outils que personne n'utilise.</p>
  <p style="margin-top:18px;font-weight:500;font-size:24px;color:rgba(0,48,70,.55)">Montants HT fictifs, pour illustrer le mécanisme.</p>
</div>{footer(5)}"""))

feat = ["Contrats et conditions d'abonnement importés au même endroit", "Échéances, préavis et clauses clés extraits", "Services et garanties en doublon repérés", "Score Volpi sur 100 pour chaque contrat"]
fhtml = "".join(f"""<li style="display:flex;gap:22px;align-items:center;margin-top:24px">
<span style="flex:none;width:40px;height:40px;border-radius:50%;background:{TEAL};color:{NAVY};font-weight:800;font-size:24px;display:flex;align-items:center;justify-content:center">✓</span><span>{f}</span></li>""" for f in feat)
slides.append(page(1080, 1350, "light", f"""
<img class="fox" src="{FOX}" style="right:-180px;top:-100px;width:700px;opacity:.12">
<div style="padding:110px 88px 0">
  <div class="eyebrow" style="font-size:26px">Votre copilote</div>
  <h2 style="margin-top:40px;font-weight:800;font-size:78px;line-height:1.06;letter-spacing:-.02em">Volpi ne décide pas à votre place. Il rend visible <span class="blue">ce que vous ne lisez pas</span>.</h2>
  <ul style="list-style:none;margin-top:40px;font-weight:700;font-size:33px;line-height:1.3">{fhtml}</ul>
  <div style="margin-top:56px;background:linear-gradient(120deg,{BLUE},{TEAL2});color:#fff;border-radius:28px;padding:36px 44px">
    <div style="font-weight:800;font-size:38px;line-height:1.25">Combien vos abonnements oubliés vous coûtent&#8209;ils&nbsp;?</div>
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
