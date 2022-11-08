#-*- codeing = utf-8 -*-
#@Time:2022/2/25 13:48
#@Author:王远辉
#@File:bs4_02_self.py
#@Software:PyCharm

import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umeitu.com/bizhitupian/weimeibizhi/"
response = requests.get(url)
response.encoding = "utf-8"

# print(response.text)
# 将网页源代码放入到 bs4 中

document = BeautifulSoup(response.text,"html.parser")
alist = document.find("div", class_="TypeList").find_all("a")
for a in alist:
    href = a.get("href")
    # print(href.split("/")[-1])
    children_href = url + href.split("/")[-1]
    children_response = requests.get(children_href)
    children_response.encoding = "utf-8"
    children_document = BeautifulSoup(children_response.text,"html.parser")
    img = children_document.find("div", class_="ImageBody").find("img")
    img_src = img.get("src")
    # print(img_src)
    img_name = img_src.split("/")[-1]
    print(img_src)
    img_response = requests.get(img_src)
    img_response.encoding="utf-8"
    # print(img_name)
    with open("img/" + img_name, mode="wb") as f:
        f.write(img_response.content)
    time.sleep(1)
    print("over !", img_name)
print("all over!")

