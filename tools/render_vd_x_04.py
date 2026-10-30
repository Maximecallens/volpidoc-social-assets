# Visuel X vd_x_04 (30/10/2026) : indexation, la hausse déjà signée. Réutilise l'en-tête de render_semaine1.py.
import asyncio, os
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_semaine1.py")
src = open(SRC, encoding="utf-8").read().split("# ---------- LI-1")[0]
exec(src)

vals = [round(1200 * 1.04 ** i) for i in range(5)]  # 1200, 1248, 1298, 1350, 1404
mx = 1404
bars = ""
for i, v in enumerate(vals):
    h = int(270 * v / mx)
    last = i == 4
    col = ORANGE if last else TEAL
    bars += f"""<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end">
<div style="font-weight:800;font-size:{30 if last else 24}px;color:{ORANGE if last else NAVY};white-space:nowrap;margin-bottom:10px">{str(v)[0]}&#8239;{str(v)[1:]}&nbsp;€</div>
<div style="width:100%;height:{h}px;border-radius:14px 14px 4px 4px;background:{col};opacity:{1 if last else .55 + i*.1}"></div>
<div style="font-weight:700;font-size:22px;color:rgba(0,48,70,.6);margin-top:12px">An {i+1}</div></div>"""

chips = "".join(f"""<span style="display:inline-block;font-weight:800;font-size:32px;padding:12px 28px;border-radius:99px;background:#fff;border:3px solid {TEAL};margin-right:18px">« {w} »</span>""" for w in ["indexation", "indice", "révision"])

x4 = page(1600, 900, "dark", f"""
<img class="fox" src="{FOX}" style="right:-140px;top:-90px;width:620px;opacity:.12">
<div style="position:absolute;left:96px;top:80px;width:620px;height:500px;border-radius:36px;background:#fff;box-shadow:0 2px 0 rgba(0,48,70,.06);padding:34px 40px 26px;display:flex;flex-direction:column">
  <div style="font-weight:800;font-size:22px;letter-spacing:.12em;text-transform:uppercase;color:{TEAL2}">Même contrat, indexé de 4 % par an</div>
  <div style="flex:1;display:flex;gap:22px;align-items:flex-end;margin-top:16px">{bars}</div>
  <div style="font-weight:500;font-size:19px;color:rgba(0,48,70,.5);margin-top:14px">Exemple illustratif, montants annuels arrondis.</div>
</div>
<div style="position:absolute;left:780px;right:96px;top:92px">
  <div class="eyebrow" style="font-size:24px">Le vrai coût de vos contrats</div>
  <h1 style="margin-top:22px;font-weight:800;font-size:64px;line-height:1.1;letter-spacing:-.02em">La hausse la plus discrète est celle que vous avez <span class="teal">déjà signée.</span></h1>
  <p style="margin-top:26px;font-weight:700;font-size:34px;line-height:1.35"><span class="or">+ 204 € par an</span> en année 5, sans aucune renégociation.</p>
</div>
<div style="position:absolute;left:96px;right:96px;top:630px">
  <div style="font-weight:800;font-size:24px;letter-spacing:.1em;text-transform:uppercase;color:{TEAL2};margin-bottom:18px">Le réflexe : cherchez dans vos contrats</div>
  {chips}
</div>
<div style="position:absolute;left:96px;bottom:40px;font-weight:500;font-size:20px;color:rgba(0,48,70,.5)">Volpidoc est une aide à la lecture : ni courtier, ni conseil juridique.</div>
<img src="{LOGO_H}" style="position:absolute;right:96px;bottom:40px;height:50px">
""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1600, "height": 900})
        await pg.set_content(x4)
        await pg.wait_for_timeout(300)
        await pg.screenshot(path=f"{OUT}/x.png")
        await b.close()
asyncio.run(main())
print("ok")
