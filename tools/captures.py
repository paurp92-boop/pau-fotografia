"""Captures de la web (mòbil 390 px, x2) en ca/es/en + posicions dels apartats, per a l'editor d'Instagram.
Ús: python3 tools/captures.py <url> <carpeta_sortida>"""
import sys,json,io
from playwright.sync_api import sync_playwright
from PIL import Image
url,out=sys.argv[1],sys.argv[2]
import os;os.makedirs(out,exist_ok=True)
pos={}
with sync_playwright() as p:
    b=p.chromium.launch(args=['--no-sandbox'],executable_path=os.environ.get('CHROME') or None)
    for l in ['ca','es','en']:
        ctx=b.new_context(viewport={'width':390,'height':844},device_scale_factor=2)
        ctx.add_init_script("sessionStorage.setItem('promoSeen','1')")
        pg=ctx.new_page();pg.goto(url);pg.wait_for_timeout(1500)
        pg.evaluate(f"setLang('{l}')");pg.wait_for_timeout(1200)
        pg.evaluate("document.fonts&&document.fonts.ready");pg.wait_for_timeout(500)
        t=lambda s:pg.evaluate("s=>{const e=document.querySelector(s);return e?Math.round((e.getBoundingClientRect().top+scrollY)*2):0}",s)
        pos[l]=[0,660,max(0,t('.slider.multi')-1),max(0,t('.com1m')-47),max(0,t('.pack')-180),99999]
        im=Image.open(io.BytesIO(pg.screenshot(full_page=True))).convert('RGB')
        im.save(f'{out}/web-full-{l}.jpg',quality=88);ctx.close()
    b.close()
json.dump(pos,open(f'{out}/web-pos.json','w'))
print(pos)
