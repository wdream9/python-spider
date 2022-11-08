# -*- codeing = utf-8 -*-
# @Time:2022/2/25 11:27
# @Author:王远辉
# @File:re_02_2.py
# @Software:PyCharm
import requests
import csv
import re

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; IntelMac OS X 10_15_4) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 87.0.4280.88Safari / 537.36"
}
url = "https://movie.douban.com/top250?start = 0 & filter = "
resp = requests.get(url, headers=headers)
# print(resp.text)

obj = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>', re.S)

it = obj.finditer(resp.text)
with open("movie.csv", mode="w", encoding="utf-8") as f:
    csvwriter = csv.writer(f)  # 创建csv⽂件写⼊⼯具,也可以直接f.write()
for item in it:
    dic = item.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())  # 写⼊数
f.close()