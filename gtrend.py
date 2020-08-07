from pytrends.request import TrendReq

# code from https://zhuanlan.zhihu.com/p/113839732

pytrends = TrendReq(hl='zh-Hans', tz=360) # 时区指定为“中央标准时区”，即“ 360”
pytrends.build_payload(['Coronavirus'], cat=0, timeframe='2020-02-01 2020-03-10',  gprop='', geo='US-NY')

df = pytrends.interest_over_time()
print(df.head())