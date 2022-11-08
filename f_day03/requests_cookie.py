#-*- codeing = utf-8 -*-
#@Time:2022/2/25 17:10
#@Author:王远辉
#@File:requests_cookie.py
#@Software:PyCharm

import requests
# 爬取需要登录后的网站
# 会话
session = requests.session()
data = {

}

# 1、登录
url = ""
response = session.post(url,data=data)
# print(response.text)
# print(response.cookies) #查看cookie

# 登陆后使用 session 中的cookie
url2 = ""
response1 = session.get(url2)
print(response1.text)
print(response1.json())