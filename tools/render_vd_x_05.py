# Visuel X vd_x_05 (04/11/2026) : après le 31/10, frise des 6 prochains mois. Réutilise l'en-tête de render_semaine1.py.
import asyncio, os
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "render_semaine1.py")
src = open(SRC, encoding="utf-8").read().split("# ---------- LI-1")[0]
exec(src)

months = ["Nov.", "Déc.", "Janv.", "Févr.", "Mars", "Avr."]
# échéances illustratives : (index mois, libellé, préavis)
events = {1: ("Logiciel", "préavis 1 mois"), 2: ("Assurance", "préavis 2 mois"), 3: ("Télécom", "préavis 1 mois"), 5: ("Maintenance", "préavis 3 mois")}
cols = ""
for i, m in enumerate(months):
    ev = events.get(i)
    card = ""
    if ev:
        card = f"""<div style="position:absolute;bottom:40px;left:50%;transform:translateX(-50%);width:190px;background:#fff;border-radius:18px;padding:16px 14px;text-align:center;box-shadow:0 2px 0 rgba(0,48,70,.06);border-top:6px solid {TEAL}">
<div style="font-weight:800;font-size:26px">{ev[0]}</div><div style="font-weight:700;font-size:20px;color:{ORANGE};margin-top:6px">{ev[1]}</div></div>"""
    dot = f"""<div style="position:absolute;bottom:-13px;left:50%;transform:translateX(-50%);width:{28 if ev else 16}px;height:{28 if ev else 16}px;border-radius:50%;background:{ORANGE if ev else 'rgba(0,48,70,.25)'};{'border:5px solid #fff;box-sizing:content-box' if ev else 'bottom:-8px'}"></div>"""
    cols += f"""<div style="flex:1;position:relative">{card}{dot}
<div style="position:absolute;top:256px;width:100%;text-align:center;font-weight:800;font-size:26px;color:rgba(0,48,70,.7)">{m}</div></div>"""

x5 = page(1600, 900, "dark", f"""
<img class="fox" src="{FOX}" style="right:-140px;top:-90px;width:620px;opacity:.12">
<div style="position:absolute;left:96px;right:96px;top:80px">
  <div class="eyebrow" style="font-size:24px">Reprendre la main</div>
  <h1 style="margin-top:20px;font-weight:800;font-size:66px;line-height:1.08;letter-spacing:-.02em">Le 31/10 est passé ? <span class="teal">Tout n'est pas joué.</span></h1>
  <p style="margin-top:22px;font-weight:700;font-size:32px;line-height:1.35;max-width:1100px">Toutes les échéances ne tombent pas au 1<sup>er</sup> janvier. Listez celles des <span class="or" style="white-space:nowrap">6&nbsp;prochains mois</span>, préavis compris.</p>
</div>
<div style="position:absolute;left:96px;right:96px;top:400px;height:300px">
  <div style="position:absolute;left:0;right:0;top:220px;height:6px;border-radius:3px;background:linear-gradient(90deg,{TEAL},rgba(0,148,182,.25))"></div>
  <div style="position:absolute;left:0;right:0;top:226px;bottom:0;display:flex">{''.join(f'<div style="flex:1"></div>' for _ in months)}</div>
  <div style="position:absolute;left:0;right:0;top:0;height:226px;display:flex;overflow:visible">{cols}</div>
</div>
<div style="position:absolute;left:96px;top:790px;font-weight:500;font-size:20px;color:rgba(0,48,70,.5)">Exemple illustratif. Volpidoc est une aide à la lecture : ni courtier, ni conseil juridique.</div>
<img src="{LOGO_H}" style="position:absolute;right:96px;bottom:44px;height:50px">
""")

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1600, "height": 900})
        await pg.set_content(x5)
        await pg.wait_for_timeout(300)
        await pg.screenshot(path=f"{OUT}/x.png")
        await b.close()
asyncio.run(main())
print("ok")
