#-*- codeing = utf-8 -*-
#@Time:2022/3/19 20:55
#@Author:王远辉
#@File:yang.py
#@Software:PyCharm

from lxml import etree

file = open("./index.html",mode='r')
tree = etree.HTML(file)
print(tree)
