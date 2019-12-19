import requests
from lxml import etree
from s11月机试考试.User_agent_name import my_chrome_agent
import random
import re
headers={
    'User-Agent':random.choice(my_chrome_agent)
}
urls=[
    # 'http://www.hao123.com/music/wangzhi',
      # 'http://music.taihe.com/?fr=hao123',
      'http://www.app-echo.com/#/'
      ]
for url in urls:
    res=requests.get(url)
    res.encoding=res.apparent_encoding
# print(res.text)
    soup=etree.HTML(res.text,etree.HTMLParser())
    list_info=soup.xpath('//a[@class="text-con"]')#主网页
    list_info1=soup.xpath('//a[@class="img-wrapper pr"]')#千千音乐界面
    list_info2=soup.xpath('//img[@class="pic"]/@src')#echo界面
    # list_info2=re.findall('<img src="(.*?)">',res.text)
    print(list_info2)
    print('++++++++++++++++++++++++++++++++++++++++++++++++')
    # for info in list_info1:
    #     mess=info.get('href')
    #     print('http://music.taihe.com/'+mess)
    #     print('-------------------------------------------')
    # for inf in list_info:
    #     res=inf.get('href')
    #     print(res)
    #     print('*********************************************')
    # for img in list_info2:
    #     ress=img.get('src')
    #     print(ress)