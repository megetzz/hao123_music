# 'http://www.hao123.com/music/wangzhi'

import requests
from bs4 import BeautifulSoup

url='http://www.hao123.com/music/wangzhi'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
proxies={
    'http':'58.218.201.114:4355'
}
res=requests.get(url,headers=headers,proxies=proxies)
# print(res.status_code)
# print(res.text)
res.encoding=res.apparent_encoding

soup=BeautifulSoup(res.text,'html.parser')
#bd > div:nth-child(1) > div > ul > li:nth-child(2) > h3 > div > a
html=soup.select('#bd > div > div > ul > li > h3 > div > a ')
# print(html)
for i in html:
    h=i.get('href')
    # t=i.get('text')
    print(h)
    # print(t)
    with open('hao123_music','a',encoding='utf8')as f:
        f.write(h+'\n')