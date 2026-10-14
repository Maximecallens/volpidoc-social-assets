import asyncio, base64, os
from playwright.async_api import async_playwright

A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
OUT = os.environ.get("OUT", "out")
os.makedirs(OUT, exist_ok=True)

def b64(p):
    return base64.b64encode(open(p, "rb").read()).decode()

FONTS = "".join(
    f"@font-face{{font-family:'PJS';font-weight:{w};src:url(data:font/woff2;base64,{b64(f'{A}/plus-jakarta-sans-latin-{w}-normal.woff2')}) format('woff2');}}"
    for w in (500, 700, 800)
)
LOGO_H = "data:image/png;base64," + b64(f"{A}/logo-h.png")
LOGO_H_W = "data:image/png;base64," + b64(f"{A}/logo-h-white.png")
FOX = "data:image/png;base64," + b64(f"{A}/fox.png")

NAVY, TEAL, TEAL2, BLUE, ORANGE = "#003046", "#64C5C1", "#26A7BA", "#0094B6", "#F15A24"
LIGHT = "#F2F8F8"

BASE = f"""
{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:var(--w);height:var(--h);overflow:hidden}}
body{{font-family:'PJS','Inter',sans-serif;-webkit-font-smoothing:antialiased;position:relative}}
.dark{{background:linear-gradient(165deg,#FFFFFF 0%,#EAF6F5 55%,#D9F0EE 100%);color:{NAVY}}}
.light{{background:{LIGHT};color:{NAVY}}}
.eyebrow{{font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:{ORANGE}}}
.teal{{color:{BLUE}}} .blue{{color:{BLUE}}} .or{{color:{ORANGE}}}
.fox{{position:absolute;opacity:.10;pointer-events:none}}
"""

def page(w, h, cls, body, extra=""):
    import re
    body = re.sub(r" ([?:;!])(?=[\s<])", "&nbsp;\\1", body)
    body = body.replace(" ?<", "&nbsp;?<").replace(" ?\"", "&nbsp;?\"")
    return f"<!doctype html><html><head><meta charset='utf-8'><style>:root{{--w:{w}px;--h:{h}px}}{BASE}{extra}</style></head><body class='{cls}'>{body}</body></html>"

def timeline(scale=1.0, dark=False):
    s = scale
    txt = "#fff" if dark else NAVY
    sub = "rgba(255,255,255,.65)" if dark else "rgba(0,48,70,.6)"
    track = "rgba(255,255,255,.18)" if dark else "rgba(0,48,70,.12)"
    return f"""
<div style="position:relative;height:{190*s}px">
  <div style="position:absolute;left:0;right:0;top:{70*s}px;height:{10*s}px;border-radius:99px;background:{track}"></div>
  <div style="position:absolute;left:8%;right:8%;top:{70*s}px;height:{10*s}px;border-radius:99px;background:linear-gradient(90deg,{ORANGE},{TEAL})"></div>
  <div style="position:absolute;left:8%;top:{56*s}px;width:{38*s}px;height:{38*s}px;margin-left:{-19*s}px;border-radius:50%;background:{ORANGE};box-shadow:0 0 0 {10*s}px rgba(241,90,36,.25)"></div>
  <div style="position:absolute;right:8%;top:{56*s}px;width:{38*s}px;height:{38*s}px;margin-right:{-19*s}px;border-radius:50%;background:{TEAL}"></div>
  <div style="position:absolute;left:8%;top:0;transform:translateX(-50%);font-weight:800;font-size:{30*s}px;color:{ORANGE};white-space:nowrap">31 octobre</div>
  <div style="position:absolute;right:8%;top:0;transform:translateX(50%);font-weight:800;font-size:{30*s}px;color:{txt};white-space:nowrap">1er janvier</div>
  <div style="position:absolute;left:8%;top:{118*s}px;transform:translateX(-50%);font-weight:500;font-size:{24*s}px;color:{sub};text-align:center;line-height:1.3;white-space:nowrap">dernier jour<br>pour prévenir</div>
  <div style="position:absolute;right:8%;top:{118*s}px;transform:translateX(50%);font-weight:500;font-size:{24*s}px;color:{sub};text-align:center;line-height:1.3;white-space:nowrap">échéance<br>du contrat</div>
  <div style="position:absolute;left:50%;top:{102*s}px;transform:translateX(-50%);font-weight:700;font-size:{24*s}px;color:{txt};background:{'rgba(255,255,255,.08)' if dark else '#fff'};padding:{8*s}px {18*s}px;border-radius:99px;white-space:nowrap">2 mois de préavis</div>
</div>"""

# ---------- LI-1 (1080x1350) ----------
li1 = page(1080, 1350, "dark", f"""
<img class="fox" src="{FOX}" style="right:-170px;top:-60px;width:760px;opacity:.12">
<div style="padding:96px 88px 0">
  <div class="eyebrow" style="font-size:26px">Série · Avant le 31/12</div>
  <h1 style="margin-top:44px;font-weight:800;font-size:76px;line-height:1.08;letter-spacing:-.02em">
    Ce que vous <span class="teal">ne lisez pas</span> dans vos contrats vous coûte plus cher que ce que vous négociez mal.
  </h1>
</div>
<div style="position:absolute;left:88px;right:88px;top:660px">{timeline(1.15)}<div style="margin-top:34px;font-weight:500;font-size:24px;color:rgba(0,48,70,.55)">Exemple : contrat à échéance au 1er janvier, préavis de 2 mois.</div></div>
<div style="position:absolute;left:88px;right:88px;bottom:88px;display:flex;align-items:flex-end;justify-content:space-between">
  <div style="font-weight:500;font-size:28px;line-height:1.4;color:rgba(0,48,70,.75);max-width:560px">Volpi lit vos contrats et vous montre ce qui vous échappe.</div>
  <img src="{LOGO_H}" style="height:64px">
</div>
""")

# ---------- X-1 (1600x900) ----------
x1 = page(1600, 900, "dark", f"""
<img class="fox" src="{FOX}" style="right:-120px;top:-80px;width:640px;opacity:.12">
<div style="padding:84px 96px 0">
  <div class="eyebrow" style="font-size:24px">Avant le 31/12</div>
  <h1 style="margin-top:30px;font-weight:800;font-size:64px;line-height:1.1;letter-spacing:-.02em;max-width:1180px">
    Ce que vous <span class="teal">ne lisez pas</span> dans vos contrats coûte plus cher que ce que vous négociez mal.
  </h1>
</div>
<div style="position:absolute;left:96px;right:96px;top:520px">{timeline(1.0)}</div>
<img src="{LOGO_H}" style="position:absolute;right:96px;bottom:64px;height:52px">
""")

# ---------- X-2 (1600x900) ----------
qs = ["Avant quelle date dois-je prévenir pour en sortir ?",
      "Qu'est-ce qui a changé depuis la signature ?",
      "Est-ce que je paie deux fois le même risque ?"]
qhtml = "".join(f"""
<div style="display:flex;align-items:center;gap:32px;background:#fff;border-radius:24px;padding:30px 40px;box-shadow:0 2px 0 rgba(0,48,70,.06)">
  <div style="flex:none;width:72px;height:72px;border-radius:18px;background:{BLUE};color:#fff;font-weight:800;font-size:36px;display:flex;align-items:center;justify-content:center">{i+1}</div>
  <div style="font-weight:700;font-size:40px;line-height:1.2">{q}</div>
</div>""" for i, q in enumerate(qs))
x2 = page(1600, 900, "light", f"""
<img class="fox" src="{FOX}" style="right:-140px;bottom:-140px;width:620px;opacity:.12">
<div style="padding:72px 96px 0">
  <div class="eyebrow" style="font-size:24px">Avant le 31/10</div>
  <h1 style="margin-top:20px;font-weight:800;font-size:58px;letter-spacing:-.02em">3 questions à poser à <span class="blue">chaque contrat</span></h1>
  <div style="margin-top:44px;display:flex;flex-direction:column;gap:22px;max-width:1220px">{qhtml}</div>
</div>
<div style="position:absolute;left:96px;bottom:62px;font-weight:700;font-size:32px">Une réponse vous échappe ? <span class="or">C'est un angle mort.</span></div>
<img src="{LOGO_H}" style="position:absolute;right:96px;bottom:56px;height:50px">
""")

# ---------- Carousel (7 x 1080x1350) ----------
def footer(n, dark):
    logo = LOGO_H
    col = "rgba(0,48,70,.5)"
    return f"""<div style="position:absolute;left:88px;right:88px;bottom:72px;display:flex;justify-content:space-between;align-items:center">
<img src="{logo}" style="height:48px"><div style="font-weight:700;font-size:26px;color:{col}">{n} / 7</div></div>"""

def clause(n, title, lead, checks, dark, tag):
    col = "rgba(0,48,70,.8)"
    card = "#fff;box-shadow:0 2px 0 rgba(0,48,70,.06)"
    chk = "".join(f"""<li style="display:flex;gap:22px;align-items:flex-start;margin-top:22px">
<span style="flex:none;margin-top:6px;width:30px;height:30px;border-radius:8px;border:3px solid {TEAL}"></span>
<span>{c}</span></li>""" for c in checks)
    body = f"""
<img class="fox" src="{FOX}" style="right:-200px;top:-120px;width:640px;opacity:.10">
<div style="position:absolute;inset:96px 88px 170px;display:flex;flex-direction:column">
  <div style="display:flex;align-items:baseline;gap:24px">
    <div style="font-weight:800;font-size:150px;line-height:.9;color:{ORANGE}">0{n}</div>
    <div class="eyebrow" style="font-size:24px;color:{TEAL2}">{tag}</div>
  </div>
  <h2 style="margin-top:44px;font-weight:800;font-size:76px;line-height:1.08;letter-spacing:-.02em">{title}</h2>
  <p style="margin-top:34px;font-weight:500;font-size:40px;line-height:1.4;color:{col}">{lead}</p>
  <div style="margin-top:auto;background:{card};border-radius:28px;padding:36px 44px 44px">
    <div style="font-weight:800;font-size:26px;letter-spacing:.1em;text-transform:uppercase;color:{TEAL2}">À vérifier</div>
    <ul style="list-style:none;font-weight:600;font-size:37px;line-height:1.35">{chk}</ul>
  </div>
</div>{footer(n+1, dark)}"""
    return page(1080, 1350, "dark" if dark else "light", body)

slides = []
slides.append(page(1080, 1350, "dark", f"""
<img class="fox" src="{FOX}" style="right:-220px;bottom:-160px;width:900px;opacity:.12">
<div style="padding:110px 88px 0">
  <div class="eyebrow" style="font-size:28px">Série · Avant le 31/12</div>
  <h1 style="margin-top:56px;font-weight:800;font-size:104px;line-height:1.02;letter-spacing:-.025em"><span class="or">5 clauses</span> à relire avant que vos contrats se renouvellent <span class="teal">tout seuls</span>.</h1>
  <p style="margin-top:48px;font-weight:500;font-size:36px;line-height:1.4;color:rgba(0,48,70,.75);max-width:820px">Assurance ou fournisseurs : les mauvaises surprises se cachent presque toujours aux mêmes endroits.</p>
</div>
<div style="position:absolute;left:88px;bottom:170px;font-weight:700;font-size:32px;color:{BLUE}">Faites défiler →</div>
{footer(1, True)}"""))
data = [
    ("La date qui compte, c'est la date limite pour prévenir.", "L'échéance au 1er janvier avec 2 mois de préavis ? Votre courrier doit partir avant le 31&nbsp;octobre.",
     ["La date d'échéance exacte", "La durée du préavis", "La forme exigée (recommandé, e-mail, espace client…)"], "Échéance & préavis"),
    ("Sans courrier de votre part, le contrat repart.", "La tacite reconduction relance souvent le contrat pour une nouvelle année complète.",
     ["La durée de reconduction", "Les conditions de sortie en cours de contrat", "Les frais en cas de résiliation anticipée"], "Tacite reconduction"),
    ("Le prix signé n'est pas toujours le prix payé.", "Indexation annuelle, paliers, options ajoutées en route : la facture dérive sans bruit.",
     ["La clause d'indexation ou de révision", "Le prix actuel face au prix d'origine", "Les options que vous n'utilisez plus"], "Révision de prix"),
    ("Assuré, oui. Mais à partir de combien, et jusqu'à combien ?", "Une garantie n'a de valeur qu'avec sa franchise et son plafond.",
     ["Le montant de la franchise", "Le plafond par sinistre et par an", "Les sous-limites propres à certaines garanties"], "Franchises & plafonds"),
    ("Ce qui n'est pas couvert… et ce qui l'est deux fois.", "Les exclusions laissent des trous ; les doublons font payer deux fois le même risque.",
     ["Les exclusions qui touchent votre activité", "Les garanties présentes dans deux contrats", "Ce qui a changé dans votre activité depuis la signature"], "Exclusions & doublons"),
]
for i, (t, l, c, tag) in enumerate(data, start=1):
    slides.append(clause(i, t, l, c, dark=(i % 2 == 0), tag=tag))

feat = ["Échéances et préavis extraits automatiquement", "Clauses clés et Score Volpi sur 100", "Garanties en doublon détectées", "Lettre de résiliation pré-remplie"]
fhtml = "".join(f"""<li style="display:flex;gap:22px;align-items:center;margin-top:24px">
<span style="flex:none;width:40px;height:40px;border-radius:50%;background:{TEAL};color:{NAVY};font-weight:800;font-size:24px;display:flex;align-items:center;justify-content:center">✓</span><span>{f}</span></li>""" for f in feat)
slides.append(page(1080, 1350, "light", f"""
<img class="fox" src="{FOX}" style="right:-180px;top:-100px;width:700px;opacity:.12">
<div style="padding:110px 88px 0">
  <div class="eyebrow" style="font-size:26px">Votre copilote</div>
  <h2 style="margin-top:40px;font-weight:800;font-size:78px;line-height:1.06;letter-spacing:-.02em">Volpi ne décide pas à votre place. Il rend visible <span class="blue">ce que vous ne lisez pas</span>.</h2>
  <ul style="list-style:none;margin-top:40px;font-weight:700;font-size:34px;line-height:1.3">{fhtml}</ul>
  <div style="margin-top:56px;background:linear-gradient(120deg,{BLUE},{TEAL2});color:#fff;border-radius:28px;padding:36px 44px">
    <div style="font-weight:800;font-size:38px;line-height:1.25">Combien vos angles morts vous coûtent&#8209;ils&nbsp;?</div>
    <div style="margin-top:12px;font-weight:700;font-size:30px;color:#fff;opacity:.92">volpidoc.com/calculateur-roi</div>
  </div>
  <p style="margin-top:28px;font-weight:500;font-size:22px;color:rgba(0,48,70,.55)">Volpidoc est une aide à la lecture : ni courtier, ni conseil juridique.</p>
</div>{footer(7, False)}"""))

JOBS = [("li1-angle-mort.png", li1, 1080, 1350), ("x1-preavis.png", x1, 1600, 900), ("x2-3-questions.png", x2, 1600, 900)]
JOBS += [(f"li2-slide-{i+1}.png", s, 1080, 1350) for i, s in enumerate(slides)]

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for name, html, w, h in JOBS:
            pg = await b.new_page(viewport={"width": w, "height": h})
            await pg.set_content(html)
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=f"{OUT}/{name}")
            await pg.close()
        await b.close()

asyncio.run(main())
print("ok")
