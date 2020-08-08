import re
import time
import asyncio
from lxml import etree
from pyppeteer import launch

async def main():
    # headless参数设为False，则变成有头模式
    browser = await launch(
        # headless=False
    )
    page = await browser.newPage()
    await page.setViewport(viewport={'width':1280, 'height':800})
    await page.setJavaScriptEnabled(enabled=True)
    await page.goto('https://trends.google.com/trends/explore?hl=zh-Hans')
    await page.type(selector='input#input-254', text='bitcoin')
    await asyncio.sleep(1) # 等待网页加载出来，懒得用条件判断了
    await page.keyboard.press('Enter')
    await asyncio.sleep(2)
    # print(await page.title())
    await page.goto('https://trends.google.com/trends/explore?date=all&geo=CN&q=bitcoin&hl=zh-Hans')
    await asyncio.sleep(2)
    content_text = await page.content()
    # print(content_text)
    res = re.findall(r'<table>.*</table>?', content_text, flags=0)[0]
    # print(res)
    tree = etree.HTML(res)
    values = tree.xpath('//table/tbody/tr')
    for item in values:
        timeformat = item.xpath('./td[1]/text()')[0].replace('\u202a','').replace('\u202c','')
        # print(timeformat)
        timeArray = time.strptime(str(time.localtime().tm_year) + ' ' + timeformat, "%Y %b %d at %H:%M %p")
        timestamp = int(time.mktime(timeArray))
        print(timestamp) # 时间戳
        score = item.xpath('./td[2]/text()')[0]
        print(score) # 分数

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())