# -*- codeing = utf-8 -*-
# @Time:2022/2/25 12:09
# @Author:王远辉
# @File:bs4_02.py
# @Software:PyCharm

import requests
from bs4 import BeautifulSoup
import time
url = "https://www.umeitu.com/bizhitupian/weimeibizhi/"
res = requests.get(url)
res.encoding = "utf-8"
# print(res.text)

# 把页面源代码交给bs4
main_page = BeautifulSoup(res.text, "html.parser")
alist = main_page.find("div", class_="TypeList").find_all("a")
# print(alist)
for a in alist:
    href = a.get("href")  # 直接通过 get()就可以拿到属性的值
    # 拿到子页面的源代码
    children_page_res = requests.get(href)
    children_page_res.encoding = "utf-8"
    children_page_text = children_page_res.text
    # 从子页面中拿到图片的下载路径
    children_pag = BeautifulSoup(children_page_text, parser="html.parser")
    p = children_pag.find("p", align="center")
    img = p.find("img")
    src = img.get("src")
    # print(img.get("src"))
    #  下载图片
    img_res = requests.get(src)
    # img_res.content  # 拿到响应的字节流
    img_name = src.split("/")[-1]  # 拿到图片名字
    with open("img_name",mode="wb") as f:
        f.write(img_res.content)
    time.sleep(1)
    print("over" ,img_name)
    f.close()
