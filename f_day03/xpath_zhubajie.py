#-*- codeing = utf-8 -*-
#@Time:2022/2/25 16:11
#@Author:王远辉
#@File:xpath_zhubajie.py
#@Software:PyCharm
import requests
from lxml import etree


url = "https://shenzhen.zbj.com/search/f/?kw=saas"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
document = requests.get(url,headers=headers, verify=False)

tree = etree.HTML(document.text)
print(tree)