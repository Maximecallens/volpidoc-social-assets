# Carrousel LinkedIn vd_li_08 (19/11/2026) : cabinet de santé, 5 contrats fournisseurs à relire avant 2027. Réutilise l'en-tête de render_semaine1.py.
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
  <div class="eyebrow" style="font-size:28px">Santé libérale · reprendre la main</div>
  <h1 style="margin-top:56px;font-weight:800;font-size:90px;line-height:1.04;letter-spacing:-.025em">Cabinet de santé&nbsp;: <span class="or">5 contrats</span> fournisseurs à relire <span class="teal">avant 2027</span>.</h1>
  <p style="margin-top:48px;font-weight:500;font-size:36px;line-height:1.4;color:rgba(0,48,70,.75);max-width:860px">Signés à l'installation, reconduits depuis. Et la fiche d'inventaire pour les remettre à plat en une soirée.</p>
</div>
<div style="position:absolute;left:88px;bottom:170px;font-weight:700;font-size:32px;color:{BLUE}">Faites défiler →</div>
{footer(1)}"""))

slides.append(pair(2,
  (1, "Logiciel métier", "Dossier patient, agenda, facturation", "Abonnement souvent indexé chaque année, modules ajoutés au fil du temps, engagement parfois pluriannuel.", "Vérifiez la durée d'engagement et la clause d'indexation"),
  (2, "Maintenance", "Fauteuil, table, appareils", "Le contrat a souvent suivi l'achat du matériel. Le matériel a vieilli ou changé, le contrat est resté.", "Vérifiez la date d'échéance et le préavis de résiliation"),
  "light"))
slides.append(pair(3,
  (3, "Location et leasing", "Matériel loué ou financé", "Durée, loyer, option d'achat, conditions de restitution&nbsp;: la fin de contrat se prépare plusieurs mois avant.", "Notez la date de fin et ce qui se passe à l'échéance"),
  (4, "Téléphonie et secrétariat", "Lignes, standard, prise de rendez&#8209;vous", "Options cumulées, services en doublon avec l'agenda en ligne, tarif qui a bougé depuis la signature.", "Comparez ce que vous payez à ce que vous utilisez"),
  "dark"))

slides.append(page(1080, 1350, "light", f"""
<img class="fox" src="{FOX}" style="right:-200px;top:-120px;width:640px;opacity:.10">
<div style="position:absolute;inset:88px 88px 160px;display:flex;flex-direction:column;gap:34px;justify-content:center">
{step_card(5, "Déchets de soins", "Collecte des DASRI", "Fréquence de passage, nombre de contenants, tarif par collecte&nbsp;: un contrat qui suit rarement l'évolution réelle de l'activité.", "Vérifiez que la fréquence correspond encore à vos besoins")}
<div style="background:linear-gradient(120deg,{BLUE},{TEAL2});color:#fff;border-radius:28px;padding:40px 44px">
  <div style="font-weight:800;font-size:44px;line-height:1.18">Pour chacun, la même question&nbsp;:</div>
  <div style="margin-top:16px;font-weight:600;font-size:32px;line-height:1.38;opacity:.95">si je ne fais rien, que se passe-t-il à la prochaine échéance&nbsp;? Reconduction tacite, nouveau tarif, un an de plus&nbsp;?</div>
</div>
</div>{footer(4)}"""))

cols = ["Fournisseur", "Échéance", "Préavis", "Prix actuel", "Encore utilisé&nbsp;?"]
rows = [("Logiciel métier", "31/03/2027", "3 mois", "89 €/mois", "Oui"),
        ("Maintenance table", "01/01/2027", "2 mois", "420 €/an", "À revoir"),
        ("Option standard tél.", "15/06/2027", "1 mois", "25 €/mois", "Non"),
        ("", "", "", "", ""),
        ("", "", "", "", "")]
th = "".join(f'<th style="text-align:left;padding:18px 12px;font-weight:800;font-size:23px;color:#fff;background:{NAVY}">{c}</th>' for c in cols)
def cell(v, j):
    col = NAVY
    if j == 4 and v == "Non": col = ORANGE
    if j == 4 and v == "À revoir": col = BLUE
    return f'<td style="padding:20px 12px;font-weight:{800 if j==4 else 600};font-size:24px;color:{col};border-bottom:2px solid rgba(0,48,70,.08);height:76px">{v}</td>'
trs = "".join("<tr>" + "".join(cell(v, j) for j, v in enumerate(r)) + "</tr>" for r in rows)
slides.append(page(1080, 1350, "dark", f"""
<img class="fox" src="{FOX}" style="right:-200px;top:-120px;width:640px;opacity:.10">
<div style="padding:90px 88px 0">
  <div class="eyebrow" style="font-size:26px">Votre fiche d'inventaire</div>
  <h2 style="margin-top:34px;font-weight:800;font-size:68px;line-height:1.06;letter-spacing:-.02em">5 colonnes, <span class="or">une soirée</span>, et vous savez où vous en êtes.</h2>
  <div style="margin-top:44px;background:#fff;border-radius:24px;overflow:hidden;box-shadow:0 2px 0 rgba(0,48,70,.06)">
    <table style="width:100%;border-collapse:collapse">
      <tr>{th}</tr>{trs}
    </table>
  </div>
  <p style="margin-top:34px;font-weight:700;font-size:32px;line-height:1.32">Commencez par les échéances les plus proches&nbsp;: <span class="or">c'est là que le préavis se joue</span>.</p>
  <p style="margin-top:16px;font-weight:500;font-size:23px;color:rgba(0,48,70,.55)">Exemple illustratif, montants et dates fictifs. Durées et préavis varient selon chaque contrat.</p>
</div>{footer(5)}"""))

feat = ["Clauses clés de chaque contrat importé, extraites en clair", "Échéances et préavis repérés, exportables dans votre agenda", "Contrats et services en doublon signalés", "Score Volpi sur 100 pour chaque contrat"]
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
