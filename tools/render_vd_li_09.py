# Image LinkedIn vd_li_09 (24/11/2026) : consultants, RC pro et missions réellement vendues. Réutilise l'en-tête de render_semaine1.py.
import asyncio, os
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_semaine1.py")
src = open(SRC, encoding="utf-8").read().split("# ---------- LI-1")[0]
exec(src)

rows = [("Diagnostic et conseil", True), ("Formation des équipes", False),
        ("Pilotage de projet", False), ("Mise en œuvre", False)]
def row(name, ok):
    mark = (f"<span style='display:inline-flex;width:44px;height:44px;border-radius:50%;background:{TEAL};color:{NAVY};font-weight:800;font-size:24px;align-items:center;justify-content:center'>✓</span>"
            if ok else
            f"<span style='display:inline-flex;height:44px;padding:0 20px;border-radius:99px;background:{ORANGE};color:#fff;font-weight:800;font-size:23px;align-items:center'>à vérifier</span>")
    return f"""<div style="display:grid;grid-template-columns:1fr 170px 220px;align-items:center;padding:12px 0;border-top:2px solid rgba(0,48,70,.08)">
  <div style="font-weight:700;font-size:31px">{name}</div>
  <div style="text-align:center"><span style='display:inline-flex;width:44px;height:44px;border-radius:50%;background:{BLUE};color:#fff;font-weight:800;font-size:24px;align-items:center;justify-content:center'>✓</span></div>
  <div style="text-align:center">{mark}</div>
</div>"""
table = "".join(row(*r) for r in rows)

qs = [("Les activités déclarées", "décrivent-elles la mission vendue ?"),
      ("Le plafond par sinistre", "face à l'enjeu du contrat client"),
      ("Le plafond annuel", "si deux dossiers tombent la même année"),
      ("La franchise", "ce qui resterait à votre charge")]
qhtml = "".join(f"""<div style="display:flex;gap:22px;align-items:center;margin-top:18px">
  <div style="flex:none;width:44px;height:44px;border-radius:50%;background:{TEAL};color:{NAVY};font-weight:800;font-size:23px;display:flex;align-items:center;justify-content:center">{i+1}</div>
  <div style="font-size:28px;line-height:1.25"><span style="font-weight:800">{t}</span><span style="font-weight:500;color:rgba(0,48,70,.7)"> · {s}</span></div>
</div>""" for i, (t, s) in enumerate(qs))

html = page(1080, 1350, "dark", f"""
<img class="fox" src="{FOX}" style="right:-170px;top:-60px;width:760px;opacity:.12">
<div style="padding:80px 88px 0">
  <div class="eyebrow" style="font-size:26px">Conseil · Lire entre les lignes</div>
  <h1 style="margin-top:36px;font-weight:800;font-size:62px;line-height:1.08;letter-spacing:-.02em">
    Votre RC pro assure <span class="teal">ce que vous avez déclaré</span>. Pas toujours <span class="or">ce que vous vendez</span>.
  </h1>
</div>
<div style="position:absolute;left:88px;right:88px;top:430px;background:#fff;border-radius:28px;padding:26px 40px 14px;box-shadow:0 2px 0 rgba(0,48,70,.06)">
  <div style="display:grid;grid-template-columns:1fr 170px 220px;font-weight:800;font-size:21px;letter-spacing:.1em;text-transform:uppercase;color:{TEAL2};padding-bottom:12px">
    <div>Mission</div><div style="text-align:center">Vendue</div><div style="text-align:center">Déclarée</div>
  </div>
  {table}
</div>
<div style="position:absolute;left:88px;right:88px;top:842px">
  <div style="font-weight:800;font-size:25px;letter-spacing:.12em;text-transform:uppercase;color:{BLUE}">4 questions avant de signer un client</div>
  {qhtml}
</div>
<div style="position:absolute;left:88px;right:88px;bottom:72px;display:flex;align-items:flex-end;justify-content:space-between">
  <div style="font-weight:500;font-size:21px;line-height:1.4;color:rgba(0,48,70,.55);max-width:600px">Exemple illustratif. Seul votre contrat fait foi : vérifiez-le avec votre assureur.</div>
  <img src="{LOGO_H}" style="height:60px">
</div>
""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        await pg.set_content(html)
        await pg.wait_for_timeout(300)
        await pg.screenshot(path=f"{OUT}/linkedin.png")
        await b.close()
asyncio.run(main())
print("ok")
