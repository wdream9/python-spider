#-*- codeing = utf-8 -*-
#@Time:2022/2/24 21:36
#@Author:王远辉
#@File:re_01.py
#@Software:PyCharm

import  re

# findAll : 匹配字符串中所有的符合正则的内容，  返回一个列表
lst = re.findall(r"\d+","asdfhkljh1234567")
# print(lst)

# finditer： 匹配字符串中所有符合正则的内容，   返回一个迭代器
lst1 = re.finditer("\d+","asdfasdfwqer124q12341243asddfasdf3512543")
# for i in lst1:
#     print(i)

# search 返回的结果时match对象，拿数据 .group()
# 检索到一个结果就返回
res = re.search("\d+","sdfasdf28378usa09453ryiu347t9814yiou34y1")
# print(res.group())

# match 从头开始匹配
# 检索到一个就返回
str = re.match("\d+","1008asdfa12345")
# print(str.group())


# 预加载正则表达式, 先将表达式进行编译加载，
# 优点： 一个正则表达式能多次使用。

obj = re.compile("\d+", re.S)
res1 = obj.finditer("2341928duirfhqkewad9023")
# for i in res1:
#     print(i.group())

# re.S:  表示 . 能够匹配换行符
# (?P<分组名字>\d+) : 表示给 \d+ 正则表达式取一个名字
obj = re.compile("(?P<age>\d+)", re.S)

