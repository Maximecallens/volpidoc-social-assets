import asyncio, base64
from playwright.async_api import async_playwright
A="/home/claude/vd/assets"; O="/home/claude/vd/brand"
b=lambda p: base64.b64encode(open(p,'rb').read()).decode()
F="".join(f"@font-face{{font-family:PJS;font-weight:{w};src:url(data:font/woff2;base64,{b(f'{A}/plus-jakarta-sans-latin-{w}-normal.woff2')})}}" for w in (500,700,800))
FOX="data:image/png;base64,"+b(f"{A}/fox.png"); LOGO="data:image/png;base64,"+b(f"{A}/logo-h.png")
BG="linear-gradient(165deg,#FFFFFF 0%,#EAF6F5 55%,#D9F0EE 100%)"
css=f"<style>{F}*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:PJS,sans-serif;-webkit-font-smoothing:antialiased;overflow:hidden;position:relative;background:{BG}}}</style>"
def doc(w,h,body): return f"<html><head><meta charset=utf-8>{css}</head><body style='width:{w}px;height:{h}px'>{body}</body></html>"
avatar=doc(400,400,f'<img src="{FOX}" style="position:absolute;left:50%;top:50%;width:260px;transform:translate(-52%,-50%)">')
def block(h1, sub, size, subsize):
    return f'''<div style="font-weight:800;font-size:{size}px;line-height:1.1;letter-spacing:-.02em;color:#003046">Ce que vous <span style="color:#0094B6">ne lisez pas</span><br>dans vos contrats.</div>
<div style="margin-top:{int(size*.35)}px;font-weight:700;font-size:{subsize}px;white-space:nowrap;color:#F15A24;letter-spacing:.06em;text-transform:uppercase">{sub}</div>'''
# LinkedIn cover 1128x191 : logo de la page en bas à gauche -> contenu à droite
li=doc(1128,191,f'''<img src="{FOX}" style="position:absolute;left:-40px;top:-70px;width:330px;opacity:.10">
<div style="position:absolute;left:330px;right:56px;top:0;bottom:0;display:flex;align-items:center;justify-content:space-between;gap:40px">
<div>{block('', 'Le copilote IA de vos contrats · TPE, PME, indépendants', 30, 13)}</div>
<img src="{LOGO}" style="height:44px;flex:none"></div>''')
# X header 1500x500 : avatar en bas à gauche, rognage haut/bas sur mobile -> contenu centré verticalement, à droite
x=doc(1500,500,f'''<img src="{FOX}" style="position:absolute;left:-60px;top:-90px;width:560px;opacity:.10">
<div style="position:absolute;left:470px;right:90px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
<img src="{LOGO}" style="height:58px;align-self:flex-start;margin-bottom:34px">
{block('', 'Le copilote IA de vos contrats · TPE, PME, indépendants', 54, 22)}</div>''')
async def main():
  async with async_playwright() as p:
    br=await p.chromium.launch()
    for name,html,w,h,s in [("volpidoc-logo-400.png",avatar,400,400,1),("volpidoc-linkedin-banniere.png",li,1128,191,2),("volpidoc-x-banniere.png",x,1500,500,2)]:
      pg=await br.new_page(viewport={"width":w,"height":h},device_scale_factor=s); await pg.set_content(html); await pg.wait_for_timeout(300)
      await pg.screenshot(path=f"{O}/{name}"); await pg.close()
    await br.close()
asyncio.run(main())
