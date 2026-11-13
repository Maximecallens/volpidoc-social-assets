# Visuel X vd_x_08 (13/11/2026) : perte d'exploitation, boutique fermée 3 semaines. Réutilise l'en-tête de render_semaine1.py.
import asyncio, os
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_semaine1.py")
src = open(SRC, encoding="utf-8").read().split("# ---------- LI-1")[0]
exec(src)

# frise illustrative de 21 jours de fermeture : 3 premiers jours = franchise
days = ""
for d in range(1, 22):
    col = ORANGE if d <= 3 else BLUE
    op = "1" if d <= 3 else ".55"
    days += f'<div style="flex:1;height:54px;border-radius:8px;background:{col};opacity:{op}"></div>'

rows = [("1", "Perte d'exploitation", "Garantie souscrite, ou restée en option ?"),
        ("2", "Franchise en jours", "Combien de jours de fermeture restent à votre charge ?")]
checks = ""
for n, t, s in rows:
    checks += f"""<div style="display:flex;align-items:center;gap:26px;margin-top:22px">
<div style="width:62px;height:62px;border-radius:50%;background:{ORANGE};color:#fff;font-weight:800;font-size:32px;display:flex;align-items:center;justify-content:center;flex:none">{n}</div>
<div><div style="font-weight:800;font-size:32px">{t}</div><div style="font-weight:500;font-size:24px;color:rgba(0,48,70,.72);margin-top:4px">{s}</div></div></div>"""

x8 = page(1600, 900, "dark", f"""
<img class="fox" src="{FOX}" style="right:-140px;top:-90px;width:620px;opacity:.12">
<div style="position:absolute;left:96px;right:96px;top:70px">
  <div class="eyebrow" style="font-size:24px">Assurance : lire entre les lignes</div>
  <h1 style="margin-top:18px;font-weight:800;font-size:60px;line-height:1.08;letter-spacing:-.02em;white-space:nowrap">Boutique fermée 3 semaines.</h1>
  <h1 style="font-weight:800;font-size:60px;line-height:1.08;letter-spacing:-.02em;white-space:nowrap"><span class="teal">Les murs sont couverts.</span> <span class="or">Et le reste ?</span></h1>
</div>
<div style="position:absolute;left:96px;right:96px;top:300px">
  <div style="display:flex;gap:6px">{days}</div>
  <div style="display:flex;justify-content:space-between;margin-top:12px;font-weight:700;font-size:21px">
    <div class="or">Jours 1 à 3 : franchise</div>
    <div style="color:rgba(0,48,70,.6)">Loyer, salaires, charges continuent de tomber</div>
    <div class="teal">Jour 21</div>
  </div>
</div>
<div style="position:absolute;left:96px;width:1080px;top:440px;background:rgba(255,255,255,.88);border-radius:24px;padding:26px 40px 32px;box-shadow:0 2px 0 rgba(0,48,70,.06)">
  <div style="font-weight:800;font-size:20px;letter-spacing:.1em;text-transform:uppercase;color:rgba(0,48,70,.55)">Dans votre multirisque, 2 lignes à vérifier</div>
  {checks}
</div>
<div style="position:absolute;left:1226px;right:60px;top:500px;font-weight:700;font-size:30px;line-height:1.35;white-space:nowrap">On assure<br>ce qu'on possède,<br><span class="or">rarement<br>ce qu'on gagne.</span></div>
<div style="position:absolute;left:96px;top:830px;font-weight:500;font-size:20px;color:rgba(0,48,70,.5)">Exemple illustratif. Volpidoc est une aide à la lecture : ni courtier, ni conseil juridique.</div>
<img src="{LOGO_H}" style="position:absolute;right:96px;bottom:44px;height:50px">
""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1600, "height": 900})
        await pg.set_content(x8)
        await pg.wait_for_timeout(300)
        await pg.screenshot(path=f"{OUT}/x.png")
        await b.close()
asyncio.run(main())
print("ok")
