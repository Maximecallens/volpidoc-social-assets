# Visuel X vd_x_07 (11/11/2026) : deux devis au même prix, 3 lignes qui diffèrent. Réutilise l'en-tête de render_semaine1.py.
import asyncio, os
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_semaine1.py")
src = open(SRC, encoding="utf-8").read().split("# ---------- LI-1")[0]
exec(src)

# lignes illustratives : (libellé, devis A, devis B, B moins favorable ?)
rows = [("Prix annuel", "1 800 €", "1 800 €", False),
        ("Franchise", "500 €", "1 500 €", True),
        ("Plafond", "300 000 €", "150 000 €", True),
        ("Protection juridique", "incluse", "exclue", True)]
lines = ""
for i, (lab, a, b, worse) in enumerate(rows):
    bst = f"color:{ORANGE};font-weight:800" if worse else "font-weight:800"
    bd = "" if i == len(rows) - 1 else "border-bottom:1px solid rgba(0,48,70,.08);"
    lines += f"""<div style="display:flex;align-items:center;height:76px;{bd}">
<div style="width:430px;font-weight:700;font-size:28px">{lab}</div>
<div style="width:300px;font-weight:800;font-size:30px">{a}</div>
<div style="width:300px;font-size:30px;{bst}">{b}</div></div>"""

x7 = page(1600, 900, "dark", f"""
<img class="fox" src="{FOX}" style="right:-140px;top:-90px;width:620px;opacity:.12">
<div style="position:absolute;left:96px;right:96px;top:70px">
  <div class="eyebrow" style="font-size:24px">Assurance : lire entre les lignes</div>
  <h1 style="margin-top:18px;font-weight:800;font-size:60px;line-height:1.08;letter-spacing:-.02em;white-space:nowrap">Deux devis au même prix ? <span class="teal">Le vrai écart</span></h1>
  <h1 style="font-weight:800;font-size:60px;line-height:1.08;letter-spacing:-.02em;white-space:nowrap">se cache sur <span class="or">3 lignes.</span></h1>
</div>
<div style="position:absolute;left:96px;width:1030px;top:318px;background:rgba(255,255,255,.88);border-radius:24px;padding:18px 36px 14px;box-shadow:0 2px 0 rgba(0,48,70,.06)">
  <div style="display:flex;height:50px;align-items:center;font-weight:800;font-size:20px;letter-spacing:.1em;text-transform:uppercase;color:rgba(0,48,70,.55)">
    <div style="width:430px"></div><div style="width:300px">Devis A</div><div style="width:300px">Devis B</div></div>
  {lines}
</div>
<div style="position:absolute;left:1180px;right:96px;top:360px;font-weight:700;font-size:30px;line-height:1.35">Même prix,<br><span class="or">pas la même<br>couverture.</span><div style="margin-top:22px;font-weight:600;font-size:23px;color:rgba(0,48,70,.7)">Comparez ligne à ligne avant de signer.</div></div>
<div style="position:absolute;left:96px;top:820px;font-weight:500;font-size:20px;color:rgba(0,48,70,.5)">Exemple illustratif. Volpidoc est une aide à la lecture : ni courtier, ni conseil juridique.</div>
<img src="{LOGO_H}" style="position:absolute;right:96px;bottom:44px;height:50px">
""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1600, "height": 900})
        await pg.set_content(x7)
        await pg.wait_for_timeout(300)
        await pg.screenshot(path=f"{OUT}/x.png")
        await b.close()
asyncio.run(main())
print("ok")
