# Image LinkedIn vd_li_05 (17/11/2026) : BTP, ce que la décennale ne couvre pas. Réutilise l'en-tête de render_semaine1.py.
import asyncio, os
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_semaine1.py")
src = open(SRC, encoding="utf-8").read().split("# ---------- LI-1")[0]
exec(src)

rows = [("Maçonnerie", True), ("Carrelage", True), ("Étanchéité", False), ("Charpente", False)]
def row(name, ok):
    mark = (f"<span style='display:inline-flex;width:46px;height:46px;border-radius:50%;background:{TEAL};color:{NAVY};font-weight:800;font-size:26px;align-items:center;justify-content:center'>✓</span>"
            if ok else
            f"<span style='display:inline-flex;height:46px;padding:0 20px;border-radius:99px;background:{ORANGE};color:#fff;font-weight:800;font-size:24px;align-items:center'>à vérifier</span>")
    return f"""<div style="display:grid;grid-template-columns:1fr 200px 220px;align-items:center;padding:13px 0;border-top:2px solid rgba(0,48,70,.08)">
  <div style="font-weight:700;font-size:34px">{name}</div>
  <div style="text-align:center"><span style='display:inline-flex;width:46px;height:46px;border-radius:50%;background:{BLUE};color:#fff;font-weight:800;font-size:26px;align-items:center;justify-content:center'>✓</span></div>
  <div style="text-align:center">{mark}</div>
</div>"""
table = "".join(row(*r) for r in rows)

qs = [("Les activités", "listées = ce que vous facturez aujourd'hui ?"),
      ("Les exclusions", "procédés, matériaux, sous-traitance"),
      ("Plafonds et franchises", "à la mesure de vos chantiers ?")]
qhtml = "".join(f"""<div style="display:flex;gap:24px;align-items:flex-start;margin-top:24px">
  <div style="flex:none;width:46px;height:46px;border-radius:50%;background:{TEAL};color:{NAVY};font-weight:800;font-size:24px;display:flex;align-items:center;justify-content:center">{i+1}</div>
  <div><div style="font-weight:800;font-size:32px;line-height:1.15">{t}</div><div style="margin-top:4px;font-weight:500;font-size:26px;color:rgba(0,48,70,.7)">{s}</div></div>
</div>""" for i, (t, s) in enumerate(qs))

html = page(1080, 1350, "dark", f"""
<img class="fox" src="{FOX}" style="right:-170px;top:-60px;width:760px;opacity:.12">
<div style="padding:80px 88px 0">
  <div class="eyebrow" style="font-size:26px">BTP · Lire entre les lignes</div>
  <h1 style="margin-top:36px;font-weight:800;font-size:64px;line-height:1.07;letter-spacing:-.02em">
    On croit assurer <span class="teal">l'entreprise</span>. On assure souvent <span class="or">une liste d'activités</span>.
  </h1>
</div>
<div style="position:absolute;left:88px;right:88px;top:430px;background:#fff;border-radius:28px;padding:26px 40px 14px;box-shadow:0 2px 0 rgba(0,48,70,.06)">
  <div style="display:grid;grid-template-columns:1fr 200px 220px;font-weight:800;font-size:21px;letter-spacing:.1em;text-transform:uppercase;color:{TEAL2};padding-bottom:12px">
    <div>Métier</div><div style="text-align:center">Facturé</div><div style="text-align:center">Déclaré</div>
  </div>
  {table}
</div>
<div style="position:absolute;left:88px;right:88px;top:842px">
  <div style="font-weight:800;font-size:26px;letter-spacing:.12em;text-transform:uppercase;color:{BLUE}">3 questions à poser à votre attestation</div>
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
