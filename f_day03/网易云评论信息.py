#-*- codeing = utf-8 -*-
#@Time:2022/2/25 18:21
#@Author:王远辉
#@File:网易云评论信息.py
#@Software:PyCharm

# 1、找到未加密参数
# 2、想办法把参数加密
# 3、发送请求，获取信息
import requests
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="


