# -*- codeing = utf-8 -*-
# @Time:2022/2/24 22:34
# @Author:王远辉
# @File:re_02.py
# @Software:PyCharm

import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
res = requests.get(url, headers=headers)
page_content = res.text
obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>', re.S)
# 开始匹配
result = obj.finditer(page_content)
f = open("data.csv", mode="w")
csvWrite = csv.writer(f)
for item in result:
    # print(item.group("name"))
    # print(item.group("score"))
    # print(item.group("num"))
    # print(item.group("year").strip())
    dic = item.groupdict()
    dic['year'] = dic['year'].strip()
    csvWrite.writerow(dic.values())
f.close()