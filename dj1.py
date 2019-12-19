import requests
from bs4 import BeautifulSoup
import MyUserAgent
import random

url='http://www.vvvdj.com'
headers={
    'User-Agent':random.choice(MyUserAgent.my_chorme_agent)
}
res=requests.get(url,headers=headers)
print(res.status_code)
print(res.text)
# print(res.content)
