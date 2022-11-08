# -*- codeing = utf-8 -*-
# @Time:2022/8/19 14:52
# @Author:王远辉
# @File:selenium_baidu_hot_search.py
# @Software:PyCharm
from selenium.webdriver import Chrome
# chrome.find_elements_by_xpath 过时
from selenium.webdriver.common.by import By
# 无头浏览器
from selenium.webdriver.chrome.options import Options
# 对下拉框进行处理
from selenium.webdriver.support.select import Select
# 键盘事件
from selenium.webdriver.common.keys import Keys
import csv

# 配置无头浏览器
options = Options()
options.add_argument("--headless")
options.add_argument("--disbale-gpu")

chrome = Chrome(options=options)
# chrome = Chrome()
chrome.maximize_window()
chrome.get("https://top.baidu.com/buzz?b=1&fr=topindex")
chrome.implicitly_wait(10)  # 隐式等待，等待页面加载完毕，直到页面加载完成，加载完成面就不等待了
# 热手列表
div_list = chrome.find_elements(By.XPATH, '//*[@id="sanRoot"]/main/div[2]/div/div[2]/div')
print(len(div_list))
for item in div_list:
    # 标题
    title_el = item.find_element(By.XPATH, "./div[2]/a/div[1]")
    title_text = title_el.text
    # 文章链接
    article_link_el = item.find_element(By.XPATH, "./div[2]/a")
    article_link_value = article_link_el.get_attribute("href")
    print("文章标题：" + title_text)
    print("文章链接：" + article_link_value)
    print("文章标题：" + title_text)
    print("---------------------")
