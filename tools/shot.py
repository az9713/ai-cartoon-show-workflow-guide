import asyncio,sys,os
from playwright.async_api import async_playwright
TABS=sys.argv[1:]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        pg=await b.new_page(viewport={'width':2000,'height':1200},device_scale_factor=1)
        await pg.goto('file://'+os.path.abspath('index.html')+'')
        await pg.add_style_tag(content='header{display:none}.tab{padding:0}')
        await pg.evaluate("document.querySelectorAll('img').forEach(i=>i.loading='eager')")
        await pg.wait_for_function("[...document.images].every(i=>i.complete)",timeout=60000)
        for t,fn in [x.split('=') for x in TABS]:
            await pg.evaluate("t=>{show(t);zoom[t]=1;apply(document.getElementById(t))}",t)
            await pg.wait_for_timeout(400)
            el=await pg.query_selector('#'+t+' .stage')
            await el.screenshot(path=fn)
        await b.close()
asyncio.run(main())
