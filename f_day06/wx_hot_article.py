# -*- codeing = utf-8 -*-
# @Time:2022/8/23 11:23
# @Author:王远辉
# @File:wx_hot_article.py
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
chrome.get("https://fzn.cc/tushuo")
chrome.implicitly_wait(5)  # 隐式等待，等待页面加载完毕，直到页面加载完成，加载完成面就不等待了
# 热手列表
article_list = chrome.find_elements(By.XPATH, '/html/body/section/div[1]/div/article')
# print(article_list)
for index in range(len(article_list)):
    article_link_el = article_list[index].find_element(By.XPATH, './header/h2/a')
    article_link_value = article_link_el.text
    article_link_href = article_link_el.get_attribute('href')
    # print(article_link_href + "<===>" + article_link_value)
    # 爬取文章详情
    print("----------------------------------------------------")
    chrome2 = Chrome(options=options)
    chrome2.get(article_link_href)
    chrome2.implicitly_wait(2)
    article_details = chrome2.find_element(By.XPATH, '/html/body/section/div[1]/div/article/section')
    print("details==>" + article_details.text)
