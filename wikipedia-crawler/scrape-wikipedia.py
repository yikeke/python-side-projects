import json
import requests
from lxml import html

# code from https://blog.csdn.net/qubeijun/article/details/81509738

def subcat(key):
    s = requests.session()
    s.keep_alive = False
    # 拉取 url 的 html 内容
    url = 'https://zh.wikipedia.org/wiki/Category:' + key
    wiki = s.get(url)
    tree = html.fromstring(wiki.text)

    # print('https://zh.wikipedia.org/wiki/Category:' + key)
    term.append(url)
    # term.append(key) # 首行是否带 key
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
            # print('subcategories: ' + s + '\n')

    for p in pages:
        if p in term:
            pass
        else:
            term.append(p)
            # print('pages: ' + p + '\n')


term = []

w = open('year1902-2020.txt', 'w', encoding='utf-8')

for i in range(1902,2021):
    search_word = str(i) + '年出生'
    subcat(search_word)

for t in term:
    # print(type(str(t)))
    w.write(t+'\n')