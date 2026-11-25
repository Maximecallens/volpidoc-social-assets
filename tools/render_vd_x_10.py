# Visuel X vd_x_10 (25/11/2026) : RC pro consultants, missions vendues vs activités déclarées. Réutilise l'en-tête de render_semaine1.py.
import asyncio, os
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_semaine1.py")
src = open(SRC, encoding="utf-8").read().split("# ---------- LI-1")[0]
exec(src)

acts = [("Diagnostic", True), ("Recommandations", True), ("Formation des équipes", False), ("Pilotage de projet", False)]
rows = ""
for name, ok in acts:
    mark = (f'<span style="color:{BLUE};font-weight:800">Déclarée</span>' if ok
            else f'<span style="color:{ORANGE};font-weight:800">Non déclarée ?</span>')
    rows += f"""<div style="display:flex;align-items:center;justify-content:space-between;padding:16px 0;border-top:1px solid rgba(0,48,70,.12);font-size:28px">
<div style="font-weight:700">{name}</div><div style="font-size:24px">{mark}</div></div>"""

checks = ""
for n, t, s in [("1", "Activités déclarées", "Couvrent-elles les missions que vous vendez ?"),
                ("2", "Plafond par sinistre", "Suffit-il face à l'enjeu du client ?")]:
    checks += f"""<div style="display:flex;align-items:center;gap:24px;margin-top:30px">
<div style="width:60px;height:60px;border-radius:50%;background:{ORANGE};color:#fff;font-weight:800;font-size:30px;display:flex;align-items:center;justify-content:center;flex:none">{n}</div>
<div><div style="font-weight:800;font-size:30px">{t}</div><div style="font-weight:500;font-size:23px;color:rgba(0,48,70,.72);margin-top:4px">{s}</div></div></div>"""

x10 = page(1600, 900, "dark", f"""
<img class="fox" src="{FOX}" style="right:-140px;top:-90px;width:620px;opacity:.12">
<div style="position:absolute;left:96px;right:96px;top:70px">
  <div class="eyebrow" style="font-size:24px">Assurance : lire entre les lignes · Conseil</div>
  <h1 style="margin-top:18px;font-weight:800;font-size:58px;line-height:1.1;letter-spacing:-.02em">Votre RC pro couvre-t-elle ce que<br>vous vendez <span class="or">vraiment</span> ?</h1>
</div>
<div style="position:absolute;left:96px;width:700px;top:320px;background:rgba(255,255,255,.88);border-radius:24px;padding:26px 40px 20px;box-shadow:0 2px 0 rgba(0,48,70,.06)">
  <div style="font-weight:800;font-size:20px;letter-spacing:.1em;text-transform:uppercase;color:rgba(0,48,70,.55);margin-bottom:8px">Missions vendues / l'attestation</div>
  {rows}
</div>
<div style="position:absolute;left:880px;right:96px;top:320px">
  <div style="font-weight:800;font-size:20px;letter-spacing:.1em;text-transform:uppercase;color:rgba(0,48,70,.55)">Sur votre attestation, 2 lignes à vérifier</div>
  {checks}
  <div style="margin-top:40px;font-weight:700;font-size:28px;line-height:1.35">Les missions évoluent.<br><span class="teal">L'attestation, souvent pas.</span></div>
</div>
<div style="position:absolute;left:96px;top:830px;font-weight:500;font-size:20px;color:rgba(0,48,70,.5)">Exemple illustratif. Volpidoc est une aide à la lecture : ni courtier, ni conseil juridique.</div>
<img src="{LOGO_H}" style="position:absolute;right:96px;bottom:44px;height:50px">
""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1600, "height": 900})
        await pg.set_content(x10)
        await pg.wait_for_timeout(300)
        await pg.screenshot(path=f"{OUT}/x.png")
        await b.close()
asyncio.run(main())
print("ok")
