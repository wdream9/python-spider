# -*- codeing = utf-8 -*-
# @Time:2022/2/24 23:36
# @Author:王远辉
# @File:re_03.py
# @Software:PyCharm

import requests
import re

domain = "https://www.dytt89.com/"
res = requests.get(domain, verify=False)  # verify=False 去掉安全验证
res.encoding = "gb2312"  # 指定字符集
# print(res.text)
obj1 = re.compile("2020必看热片.*?<ul>(?P<ul>)</ul>", re.S)
obj2 = re.compile("<a href='(?P<href>.*?)'",re.S)
obj3 = re.compile('◎片　　名(?P<movie>.*?)<br />.*?<td '
                  'style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)

children_href_list = []
result = obj1.finditer(res.text)
for it in result:
    ul = it.group("ul")
    result_son = obj2.finditer(ul)
    for itt in result_son:
        # 拼接子页面的url地址： 域名 + 子页面地址
        children_href = domain + itt.group("href").strip("/")
        children_href_list.append(children_href)  # 把子页面连接保存起来

# 提取子页面内容
for href in children_href_list:
    children_res = requests.get(href, verify=False)
    children_res.encoding = "gb2312"  # 指定字符集

    result3 = obj3.search(children_res.text)
    print(result3.group("movie"))
    print(result3.group("download"))
    break