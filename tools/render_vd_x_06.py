# Visuel X vd_x_06 (06/11/2026) : licences payées vs utilisateurs actifs, outil par outil. Réutilise l'en-tête de render_semaine1.py.
import asyncio, os
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_semaine1.py")
src = open(SRC, encoding="utf-8").read().split("# ---------- LI-1")[0]
exec(src)

# lignes illustratives : (outil, licences payées, utilisateurs actifs, badge)
rows = [("Suite bureautique", 9, 6, None), ("Visio A", 6, 4, "doublon"), ("Visio B", 4, 2, "doublon"), ("CRM", 5, 3, None)]
def seats(paid, active):
    out = ""
    for i in range(paid):
        if i < active:
            out += f'<div style="width:38px;height:38px;border-radius:10px;background:{BLUE}"></div>'
        else:
            out += f'<div style="width:38px;height:38px;border-radius:10px;border:3px dashed {ORANGE};background:rgba(241,90,36,.08)"></div>'
    return out
lines = ""
for name, paid, active, badge in rows:
    b = f'<span style="margin-left:14px;font-weight:800;font-size:17px;letter-spacing:.08em;text-transform:uppercase;color:#fff;background:{ORANGE};padding:5px 12px;border-radius:99px">{badge}</span>' if badge else ""
    lines += f"""<div style="display:flex;align-items:center;height:72px;border-bottom:1px solid rgba(0,48,70,.08)">
<div style="width:380px;font-weight:800;font-size:28px;display:flex;align-items:center">{name}{b}</div>
<div style="display:flex;gap:12px">{seats(paid, active)}</div></div>"""

x6 = page(1600, 900, "dark", f"""
<img class="fox" src="{FOX}" style="right:-140px;top:-90px;width:620px;opacity:.12">
<div style="position:absolute;left:96px;right:96px;top:76px">
  <div class="eyebrow" style="font-size:24px">Reprendre la main</div>
  <h1 style="margin-top:18px;font-weight:800;font-size:58px;line-height:1.08;letter-spacing:-.02em;white-space:nowrap">Combien de licences payez-vous <span class="teal">pour personne ?</span></h1>
  <p style="margin-top:26px;font-weight:700;font-size:30px;line-height:1.35;max-width:1150px">Le réflexe : comparez, outil par outil, <span class="or">licences payées</span> et utilisateurs actifs.</p>
</div>
<div style="position:absolute;left:96px;width:1120px;top:350px;background:rgba(255,255,255,.85);border-radius:24px;padding:22px 36px 18px;box-shadow:0 2px 0 rgba(0,48,70,.06)">
  {lines}
  <div style="display:flex;gap:34px;margin-top:18px;font-weight:700;font-size:21px;color:rgba(0,48,70,.7)">
    <div style="display:flex;align-items:center;gap:10px"><div style="width:24px;height:24px;border-radius:7px;background:{BLUE}"></div>utilisée</div>
    <div style="display:flex;align-items:center;gap:10px"><div style="width:24px;height:24px;border-radius:7px;border:3px dashed {ORANGE};background:rgba(241,90,36,.08)"></div>payée, inutilisée</div>
  </div>
</div>
<div style="position:absolute;left:96px;top:820px;font-weight:500;font-size:20px;color:rgba(0,48,70,.5)">Exemple illustratif. Volpidoc est une aide à la lecture : ni courtier, ni conseil juridique.</div>
<img src="{LOGO_H}" style="position:absolute;right:96px;bottom:44px;height:50px">
""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1600, "height": 900})
        await pg.set_content(x6)
        await pg.wait_for_timeout(300)
        await pg.screenshot(path=f"{OUT}/x.png")
        await b.close()
asyncio.run(main())
print("ok")
