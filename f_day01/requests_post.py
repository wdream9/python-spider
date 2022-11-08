#-*- codeing = utf-8 -*-
#@Time:2022/2/24 0:10
#@Author:王远辉
#@File:requests_post.py
#@Software:PyCharm

import  requests
# 打开百度翻译

url = 'https://fanyi.baidu.com/sug'
str = input("输入英文:")
data = {
    "kw":str
}
# 发送post请求
res = requests.post(url,data=data)
# 将服务器返回的数据直接返回为 json
print(res.json())