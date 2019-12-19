import requests
from lxml import etree

def gequ(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    response.encoding = response.apparent_encoding
    content=response.text
    print(content)

    htt = etree.HTML(response.text, etree.HTMLParser())
    sult = htt.xpath('//a[@class="text-con"]')# 首页爬取
    sult1 = htt.xpath('//a[@class="img-mask pa"]')# 千千歌曲页面爬取
    sult2 = htt.xpath('//a[@class="a-link"]')
    for tab in sult:
        print(tab.get('href'))

    for tabl in sult1:
        print(tabl.get('href'))

    for tab2 in sult2:
        print(tab2.get('href'))

def main():
    urls = ['http://www.hao123.com/music/wangzhi','http://music.taihe.com/?fr=hao123','http://play.taihe.com/?__m=mboxCtrl.playSongMenu&__a=566325740&fr=web']
    for url in urls:
        gequ(url)

if __name__ == '__main__':
    main()