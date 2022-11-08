#-*- codeing = utf-8 -*-
#@Time:2022/2/25 15:24
#@Author:王远辉
#@File:xpath_02.py
#@Software:PyCharm

from lxml import etree
import requests

# etree.parse("文件路径") ：
# xpath: 元素的下标 (index) 索引是从 1 开始的
# element[index]: 表示xpth匹配的结果有很多个，可以指定拿取下标索引元素。
# element[@属性='value']：通过元素的属性值来确定我需要的是哪一元素， /a[@href="wang"]/text()： 表示选定属性值 href=”wang“ 的a标签