# -*- codeing = utf-8 -*-
# @Time:2022/2/25 14:48
# @Author:王远辉
# @File:xpath_01.py
# @Software:PyCharm

from lxml import etree

xml = """<breakfast_menu>
            <food>
                <name>Belgian Waffles</name>
                <price>$5.95</price>
                <description><span>two of our famous Belgian Waffles with plenty of real maple syrup</span></description>
                <calories>650</calories>
                <div>
                    <span>xpath111</span>
                </div>
                <span>dsasdf<span>xpath222</span></span>
                <a><span>xpath333</span></a>
            </food>
            <div><span>adefa</span></div>
        </breakfast_menu>
    """
tree = etree.XML(xml)
# text()：表示拿取文本
# result = tree.xpath("/breakfast_menu/food/name/text()") # 找到全部

# // :表示上一级标签节点所有 后代节点 包含的自定的内容
result1 = tree.xpath("/breakfast_menu//span/text()")
print(result1)

# * ：表示任意的一级节点，通配符
# result2 = tree.xpath("/breakfast_menu/*/span/text()")
# print(result2)