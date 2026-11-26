# Carrousel LinkedIn vd_li_10 (26/11/2026) : leasing et location longue durée, 6 lignes à relire avant de rendre vos véhicules. Réutilise l'en-tête de render_semaine1.py.
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
  <div class="eyebrow" style="font-size:28px">Flotte · reprendre la main</div>
  <h1 style="margin-top:56px;font-weight:800;font-size:88px;line-height:1.04;letter-spacing:-.025em">Leasing et location longue durée&nbsp;: <span class="or">6&nbsp;lignes</span> à relire <span class="teal">avant de rendre vos véhicules</span>.</h1>
  <p style="margin-top:48px;font-weight:500;font-size:36px;line-height:1.4;color:rgba(0,48,70,.75);max-width:860px">Ce qui coûte cher arrive souvent à la fin du contrat. Et la grille pour s'y prendre 6 mois avant.</p>
</div>
<div style="position:absolute;left:88px;bottom:170px;font-weight:700;font-size:32px;color:{BLUE}">Faites défiler →</div>
{footer(1)}"""))

slides.append(pair(2,
  (1, "Kilométrage", "Le plafond prévu au contrat", "Les kilomètres au-delà du forfait sont souvent facturés au retour, selon un tarif fixé à la signature.", "Comparez le compteur au forfait restant"),
  (2, "Remise en état", "Le barème de restitution", "Rayures, chocs, pneus, intérieur&nbsp;: ce qui relève de l'usure normale est défini par le contrat, pas par vous.", "Retrouvez le barème annexé au contrat"),
  "light"))
slides.append(pair(3,
  (3, "Fin et prolongation", "Ce qui se passe si vous ne faites rien", "Sans démarche de votre part, la location peut se prolonger, parfois mois après mois.", "Notez la date de fin de chaque véhicule"),
  (4, "Préavis de restitution", "Le délai pour prévenir", "Le préavis tombe souvent plusieurs mois avant la fin. C'est lui qui décide si vous gardez le choix.", "Inscrivez la date limite dans votre agenda"),
  "dark"))
slides.append(page(1080, 1350, "light", f"""
<img class="fox" src="{FOX}" style="right:-200px;top:-120px;width:640px;opacity:.10">
<div style="position:absolute;inset:88px 88px 160px;display:flex;flex-direction:column;gap:34px;justify-content:center">
{step_card(5, "Option d'achat", "Racheter ou rendre", "Prix de rachat, délai pour lever l'option, démarches&nbsp;: à connaître avant le préavis, pas après.", "Vérifiez le prix et le délai pour lever l'option")}
{step_card(6, "Services inclus", "Entretien, pneus, assistance", "Certains services peuvent faire doublon avec votre assurance flotte&nbsp;: vous payez deux fois la même chose.", "Comparez le contrat de location et l'assurance flotte")}
</div>{footer(4)}"""))

cols = ["Ligne", "Ce que dit le contrat", "Votre situation", "À faire"]
rows = [("Kilométrage", "120&nbsp;000&nbsp;km sur 48&nbsp;mois", "~135&nbsp;000&nbsp;km projetés", "Chiffrer le dépassement"),
        ("Remise en état", "Barème annexé", "2 rayures, 1&nbsp;pare&#8209;chocs", "Chiffrer avant retour"),
        ("Fin du contrat", "30/06/2027", "Prolongation si rien", "Décider avant le préavis"),
        ("Préavis", "3 mois", "Avant le 31/03/2027", "Rappel agenda"),
        ("Option d'achat", "Oui, 9&nbsp;500 € HT", "Véhicule en bon état", "Rendre ou racheter&nbsp;?"),
        ("Services inclus", "Assistance 24/7", "Aussi dans l'assurance", "Doublon à vérifier")]
th = "".join(f'<th style="text-align:left;padding:18px 14px;font-weight:800;font-size:22px;color:#fff;background:{NAVY}">{c}</th>' for c in cols)
def cell(v, j):
    col = NAVY if j < 3 else (ORANGE if j == 3 else NAVY)
    w = 800 if j in (0, 3) else 600
    return f'<td style="padding:16px 14px;font-weight:{w};font-size:22px;line-height:1.25;color:{col};border-bottom:2px solid rgba(0,48,70,.08);height:82px">{v}</td>'
trs = "".join("<tr>" + "".join(cell(v, j) for j, v in enumerate(r)) + "</tr>" for r in rows)
slides.append(page(1080, 1350, "dark", f"""
<img class="fox" src="{FOX}" style="right:-200px;top:-120px;width:640px;opacity:.10">
<div style="padding:86px 88px 0">
  <div class="eyebrow" style="font-size:26px">Votre grille · 6 mois avant la fin</div>
  <h2 style="margin-top:30px;font-weight:800;font-size:62px;line-height:1.06;letter-spacing:-.02em">6 lignes, <span class="or">une par véhicule</span>, et vous gardez le choix.</h2>
  <div style="margin-top:38px;background:#fff;border-radius:24px;overflow:hidden;box-shadow:0 2px 0 rgba(0,48,70,.06)">
    <table style="width:100%;border-collapse:collapse">
      <tr>{th}</tr>{trs}
    </table>
  </div>
  <p style="margin-top:28px;font-weight:700;font-size:30px;line-height:1.32">Commencez par le préavis&nbsp;: <span class="or">c'est la date qui décide du reste</span>.</p>
  <p style="margin-top:14px;font-weight:500;font-size:22px;color:rgba(0,48,70,.55)">Exemple illustratif d'un utilitaire, montants et dates fictifs. Clauses, durées et préavis varient selon chaque contrat.</p>
</div>{footer(5)}"""))

feat = ["Clauses clés de chaque contrat importé, extraites en clair", "Échéances et préavis repérés, exportables dans votre agenda", "Garanties et services en doublon signalés", "Score Volpi sur 100 pour chaque contrat"]
fhtml = "".join(f"""<li style="display:flex;gap:22px;align-items:center;margin-top:24px">
<span style="flex:none;width:40px;height:40px;border-radius:50%;background:{TEAL};color:{NAVY};font-weight:800;font-size:24px;display:flex;align-items:center;justify-content:center">✓</span><span>{f}</span></li>""" for f in feat)
slides.append(page(1080, 1350, "light", f"""
<img class="fox" src="{FOX}" style="right:-180px;top:-100px;width:700px;opacity:.12">
<div style="padding:110px 88px 0">
  <div class="eyebrow" style="font-size:26px">Votre copilote</div>
  <h2 style="margin-top:40px;font-weight:800;font-size:78px;line-height:1.06;letter-spacing:-.02em">Volpi ne décide pas à votre place. Il rend visible <span class="blue">ce que vous ne lisez pas</span>.</h2>
  <ul style="list-style:none;margin-top:40px;font-weight:700;font-size:33px;line-height:1.3">{fhtml}</ul>
  <div style="margin-top:56px;background:linear-gradient(120deg,{BLUE},{TEAL2});color:#fff;border-radius:28px;padding:36px 44px">
    <div style="font-weight:800;font-size:38px;line-height:1.25">Combien vos contrats mal suivis vous coûtent&#8209;ils&nbsp;?</div>
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
