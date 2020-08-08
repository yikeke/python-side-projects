from pytrends.request import TrendReq

import json
import requests
from lxml import html

# code from https://blog.csdn.net/qubeijun/article/details/81509738

# code from https://zhuanlan.zhihu.com/p/113839732

# try:
#     
# except Exception as e:
#     print(Exception,":",e)
#     print("failed to output!")

def analyze_keyword_trends(keywords, time_range):
    # The URL is https://trends.google.com/trends/explore?geo=CN&q={keyword}&hl=zh-Hans
    pytrends = TrendReq(hl='zh-Hans', tz=360) # 时区指定为“中央标准时区”，即“360”
    pytrends.build_payload(keywords, cat=0, timeframe=time_range, gprop='', geo='CN')

    df = pytrends.interest_over_time()
    # df.to_csv('result.csv',columns=[keyword]) # dataframe 数据导入 csv 文件
    df.to_csv('result.csv') # dataframe 数据导入 csv 文件
    # col_two_arr = df[keyword[0]].to_numpy() # select the keyword column values and converted them to array
    # return sum(col_two_arr), max(col_two_arr)
    col_two_arr = df.to_numpy() # select the keyword column values and converted them to array
    return col_two_arr

def subcat(key):
    term = []
    s = requests.session()
    s.keep_alive = False
    # 拉取 url 的 html 内容
    url = 'https://zh.wikipedia.org/wiki/Category:' + key
    wiki = s.get(url)
    tree = html.fromstring(wiki.text)

    print('https://zh.wikipedia.org/wiki/Category:' + key)
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

# term = []
# subcat('前1世纪出生')

# keyword = '爱因斯坦'
# time_range = '2000-07-31 2020-07-31'
# trend_data = analyze_keyword_trends(keyword, time_range)
# # print(keyword + ': total_score = ' + str(trend_data[0]) + '; max_score = ' + str(trend_data[1]))
# print(keyword + ' 的趋势：总得分为 ' + str(trend_data[0]) + '；最高得分为 ' + str(trend_data[1]))

# 打开文件
fo = open("thesaurus.txt", "r")
keywords = []
time_range = '2015-07-31 2020-07-31'

# for keyword in fo.readlines():                          #依次读取每行  
#     keyword = keyword.strip()                             #去掉每行头尾空白
#     # print(keyword, type(keyword))
#     trend_data = analyze_keyword_trends(keyword, time_range)
#     print(keyword + ' 的趋势：总得分为 ' + str(trend_data[0]) + '；最高得分为 ' + str(trend_data[1]))

# fo.close()

for keyword in fo.readlines():                          #依次读取每行  
    keyword = keyword.strip()                             #去掉每行头尾空白
    keywords.append(keyword)
    # print(keyword, type(keyword))
    # trend_data = analyze_keyword_trends(keyword, time_range)
    # print(keyword + ' 的趋势：总得分为 ' + str(trend_data[0]) + '；最高得分为 ' + str(trend_data[1]))

analyze_keyword_trends(keywords, time_range)
# print(' 的趋势：总得分为 ' + str(trend_data[0]) + '；最高得分为 ' + str(trend_data[1]))
