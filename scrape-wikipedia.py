import json
import requests
from lxml import html

w = open('thesaurus.txt', 'w', encoding='utf-8')

def subcat(key):
    s = requests.session()
    s.keep_alive = False
    # 拉取 url 的 html 内容
    url = 'https://zh.wikipedia.org/wiki/Category:' + key
    wiki = s.get(url)
    tree = html.fromstring(wiki.text)

    print('https://zh.wikipedia.org/wiki/Category:' + key)
    term.append(key)
    # 子分类
    subcategories = tree.xpath('//a[@class="CategoryTreeLabel  CategoryTreeLabelNs14 CategoryTreeLabelCategory"]/text()')
    # print(subcategories) 为 0
    pages = tree.xpath('//div[@id="mw-pages"]//a/text()')
    # print(pages) 所有的页面

    for s in subcategories:
        if s in term:
            pass
        else:
            subcat(s)
            print(s)

    for p in pages:
        if p in term:
            pass
        else:
            term.append(p)
            print(p)


term = []
subcat('前1世纪出生')
for t in term:
    w.write(t+'\n')