# -*- codeing = utf-8 -*-
# @Time:2022/2/24 0:24
# @Author:王远辉
# @File:resquests_get02.py
# @Software:PyCharm

# 当在get请求中url后面的参数比较长，不便于阅读时，可以重新封装参数
import requests

url = ""
param = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
res = requests.get(url,params=param)
# res.request.url 获取封装后的请求路径
print(res.text)
# 关闭连接
res.close()
