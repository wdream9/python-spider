# -*- codeing = utf-8 -*-
# @Time:2022/2/23 23:01
# @Author:王远辉
# @File:f_01.py
# @Software:PyCharm
# 爬虫：通过编写程序开获取互联网上的资源
# 需求： 用程序模拟浏览器，输入一个网址，从该网址中获取资源或则内容

from urllib.request import urlopen

url = 'http://www.baidu.com'
resp = urlopen(url)

with open("baidu.html", mode="w") as f:
    f.write(resp.read().decode("utf-8"))
