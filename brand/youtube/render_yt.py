import asyncio, base64
from playwright.async_api import async_playwright
A="/home/claude/vd/assets"
b=lambda p: base64.b64encode(open(p,'rb').read()).decode()
F="".join(f"@font-face{{font-family:PJS;font-weight:{w};src:url(data:font/woff2;base64,{b(f'{A}/plus-jakarta-sans-latin-{w}-normal.woff2')})}}" for w in (500,700,800))
FOX="data:image/png;base64,"+b(f"{A}/fox.png"); LOGO="data:image/png;base64,"+b(f"{A}/logo-h.png")
BG="linear-gradient(165deg,#FFFFFF 0%,#EAF6F5 55%,#D9F0EE 100%)"
base=f"<style>{F}*{{margin:0;padding:0;box-sizing:border-box}}body{{font-family:PJS,sans-serif;-webkit-font-smoothing:antialiased;overflow:hidden;position:relative}}</style>"
avatar=f"""<html><head><meta charset=utf-8>{base}</head><body style="width:800px;height:800px;background:{BG}">
<img src="{FOX}" style="position:absolute;left:50%;top:50%;width:520px;transform:translate(-52%,-50%)"></body></html>"""
banner=f"""<html><head><meta charset=utf-8>{base}</head><body style="width:2560px;height:1440px;background:{BG}">
<img src="{FOX}" style="position:absolute;right:-60px;top:240px;width:1000px;opacity:.10">
<img src="{FOX}" style="position:absolute;left:-200px;bottom:-240px;width:760px;opacity:.07;transform:scaleX(-1)">
<div style="position:absolute;left:507px;top:508px;width:1546px;height:423px;display:flex;align-items:center;justify-content:center;gap:70px;padding:0 40px">
  <img src="{LOGO}" style="height:118px;flex:none">
  <div style="flex:1;border-left:4px solid #64C5C1;padding-left:60px">
    <div style="font-weight:800;font-size:58px;line-height:1.1;letter-spacing:-.02em;color:#003046">Ce que vous <span style="color:#0094B6">ne lisez pas</span><br>dans vos contrats.</div>
    <div style="margin-top:22px;font-weight:700;font-size:27px;white-space:nowrap;color:#F15A24;letter-spacing:.06em;text-transform:uppercase">Un Short par semaine · Contrats &amp; assurances</div>
  </div>
</div></body></html>"""
async def main():
  async with async_playwright() as p:
    br=await p.chromium.launch()
    for name,html,w,h in [("volpidoc-youtube-photo.png",avatar,800,800),("volpidoc-youtube-banniere.png",banner,2560,1440)]:
      pg=await br.new_page(viewport={"width":w,"height":h}); await pg.set_content(html); await pg.wait_for_timeout(300)
      await pg.screenshot(path=f"/home/claude/vd/yt/{name}"); await pg.close()
    await br.close()
asyncio.run(main())
