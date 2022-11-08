#-*- codeing = utf-8 -*-
#@Time:2022/2/25 0:35
#@Author:王远辉
#@File:bs4_01.py
#@Software:PyCharm

# 安装 pip install bs4
# 1、拿到网页源代码
# 2、bs4进行解析

import requests
import csv
from bs4 import BeautifulSoup

url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
res = requests.get(url)
# print(res.text)
# 解析数据
# 1、把页面代码交给 BeautifulSoup进行处理，生成bs对象
page = BeautifulSoup(res.text,"html.parser")  #"html.parser" 消除警告

# 2、从bs对象中查找数据
# find(标签，属性=值)：找一个
# find_all(标签，属性=值)：找全部

# result = page.find_all("table",class="hq_table") # class_ :在这里表示html中的class，多个下划线是为了区别python中的关键字
# print(result)
table = page.find("table",attrs={
    "class": "hq_table"
})
# print(table)
# 拿到所有数据行
f = open("菜价.csv",mode="w")
csvwrite = csv.writer(f)
trs = table.find_all("tr")[1:]
for tr in trs:   # 每一行
    tds = tr.find_all("td") # 拿到每行中的所有td
    name = tds[0].text  # .text  表示拿到被标签标记的内容
    low = tds[1].text
    avg = tds[2].text
    high = tds[3].text
    gui = tds[4].text
    kind = tds[5].text
    date = tds[6].text
#     写出到文件
    csvwrite.writerow([name,low,avg,high,gui,kind,date])

f.close()
