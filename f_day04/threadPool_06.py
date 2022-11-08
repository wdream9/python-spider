# -*- codeing = utf-8 -*-
# @Time:2022/2/28 16:25
# @Author:王远辉
# @File:threadPool_06.py
# @Software:PyCharm

# 1.如何提取单个页面的数据
# 2.上线程池，抓取多个页面数据

import requests
from lxml import etree
import csv

# 准备一个文件
f = open("threadPool06.csv", mode="w", encoding="utf-8")
# csv写出到模块
csvwrite = csv.writer(f)

def download_one_page(url):
    data = {
        "limit": 20,
        "current": 2
    }
    response = requests.post(url)
    document = etree.HTML(response.text)
    print(response.text)
    table = document.xpath("/html/body/div[2]/div/div/div/div[4]/div[1]/div/table/text()")[0]
    print(table)


if __name__ == '__main__':
    url = "http://www.xinfadi.com.cn/priceDetail.html"
    download_one_page(url)