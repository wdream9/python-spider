#-*- codeing = utf-8 -*-
#@Time:2022/2/23 23:52
#@Author:王远辉
#@File:requests_01.py
#@Software:PyCharm
import requests
url = 'https://www.baidu.com/s?ie=UTF-8&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
res = requests.get(url,headers = headers)
print(res.text)
# 输出内容到文件
# with open("zhoujielun.html",mode="w") as f:
#     f.write(res.text)
