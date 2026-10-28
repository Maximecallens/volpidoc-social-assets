# Visuel X vd_x_03 (28/10/2026) : J-3, date de réception. Réutilise l'en-tête de render_semaine1.py.
import asyncio, os
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_semaine1.py")
src = open(SRC, encoding="utf-8").read().split("# ---------- LI-1")[0]
exec(src)

chk = ["La forme prévue : recommandé, e-mail, espace client…", "La date limite de réception, pas d'envoi"]
chtml = "".join(f"""<div style="display:flex;gap:24px;align-items:flex-start;margin-top:26px">
<span style="flex:none;margin-top:4px;width:34px;height:34px;border-radius:9px;border:4px solid {TEAL}"></span>
<span style="font-weight:700;font-size:36px;line-height:1.25">{c}</span></div>""" for c in chk)

x3 = page(1600, 900, "dark", f"""
<img class="fox" src="{FOX}" style="right:-140px;top:-90px;width:620px;opacity:.12">
<div style="position:absolute;left:96px;top:80px;width:400px;height:400px;border-radius:40px;background:#fff;box-shadow:0 2px 0 rgba(0,48,70,.06);display:flex;flex-direction:column;align-items:center;justify-content:center">
  <div style="font-weight:800;font-size:30px;letter-spacing:.14em;text-transform:uppercase;color:rgba(0,48,70,.55)">31 octobre</div>
  <div style="font-weight:800;font-size:190px;line-height:1;letter-spacing:-.03em;color:{ORANGE};margin-top:6px">J-3</div>
  <div style="font-weight:700;font-size:28px;color:rgba(0,48,70,.6);margin-top:8px">pour être reçu à temps</div>
</div>
<div style="position:absolute;left:576px;right:96px;top:84px">
  <div class="eyebrow" style="font-size:24px">Avant le 31/10</div>
  <h1 style="margin-top:22px;font-weight:800;font-size:62px;line-height:1.1;letter-spacing:-.02em">La date qui compte est souvent <span class="teal">la réception</span>, pas l'envoi.</h1>
  <p style="margin-top:26px;font-weight:500;font-size:30px;line-height:1.4;color:rgba(0,48,70,.72);max-width:860px">Le 31 octobre tombe un samedi : un courrier posté le vendredi arrive souvent le lundi 2 novembre.</p>
</div>
<div style="position:absolute;left:96px;right:96px;top:530px;background:#fff;border-radius:28px;padding:30px 44px 36px;box-shadow:0 2px 0 rgba(0,48,70,.06);max-width:1180px">
  <div style="font-weight:800;font-size:24px;letter-spacing:.1em;text-transform:uppercase;color:{TEAL2}">À vérifier dans le contrat</div>
  {chtml}
</div>
<div style="position:absolute;left:96px;bottom:40px;font-weight:500;font-size:20px;color:rgba(0,48,70,.5)">Volpidoc est une aide à la lecture : ni courtier, ni conseil juridique.</div>
<img src="{LOGO_H}" style="position:absolute;right:96px;bottom:40px;height:50px">
""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1600, "height": 900})
        await pg.set_content(x3)
        await pg.wait_for_timeout(300)
        await pg.screenshot(path=f"{OUT}/x.png")
        await b.close()
asyncio.run(main())
print("ok")
