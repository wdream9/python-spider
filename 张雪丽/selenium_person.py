# -*- codeing = utf-8 -*-
# @Time:2022/3/2 12:10
# @Author:王远辉
# @File:selenium_boss_01.py
# @Software:PyCharm

# 文件
import csv
# 编码
import codecs
import time
# 浏览器驱动
from selenium.webdriver import Chrome
# chrome.find_elements_by_xpath 过时
from selenium.webdriver.common.by import By
# 无头浏览器
from selenium.webdriver.chrome.options import Options

# 对下拉框进行处理
# from selenium.webdriver.support.select import Select
# 键盘事件
# from selenium.webdriver.common.keys import Keys


# 配置无头浏览器
options = Options()
# options.add_argument("--headless")
# options.add_argument("--disbale-gpu")
options.add_argument('ignore-certificate-errors')
chrome = Chrome(options=options)
# chrome = Chrome()
chrome.get("https://data.stats.gov.cn/easyquery.htm?cn=C01")
chrome.implicitly_wait(10)  # 隐式等待，等待页面加载完毕，直到页面加载完成，加载完成面就不等待了
# 获取指标
# chrome.find_element(By.XPATH, '//*[@id="treeZhiBiao_1_a"]').click()
# 获取人口
chrome.find_element(By.XPATH, '//*[@id="treeZhiBiao_4_a"]').click()
# 点击总人口
# chrome.find_element(By.XPATH, '//*[@id="treeZhiBiao_4_a"]').click()

time.sleep(1)
# 定位到下拉列表
chrome.find_element(By.XPATH, '//*[@id="mySelect_sj"]/div[2]/div[1]').click()
# select_element = chrome.find_element(By.XPATH,)
chrome.find_element(By.XPATH, '//*[@id="mySelect_sj"]/div[2]/div[2]/div[3]/input').send_keys("1949-2019")
# 输入年份点击确认
chrome.find_element(By.XPATH, '//*[@id="mySelect_sj"]/div[2]/div[2]/div[3]/div[1]').click()
# 点击总人口
chrome.find_element(By.XPATH, '//*[@id="treeZhiBiao_30_a"]').click()
# 数据转置
# chrome.find_element(By.XPATH, '//*[@id="rightmenu"]/ul/li[3]/a').click()
# 处理下拉框
# select = chrome.find_element(By.XPATH, '//*[@id="rightmenu"]/ul/li[3]/a')
# 让浏览器调整选项
# select_options = Select(select)
# select_options.select_by_index(2)

# 定位到当前 表格元素（table）
table_main = chrome.find_element(By.XPATH, '//*[@id="table_main"]')
time.sleep(1)
# 获取年份时间
years_ths = table_main.find_elements(By.XPATH, './thead/tr/th')
years = []
for th in years_ths:
    # 第一个元素是： "指标"
    years.append(th.text)
    # print(th.text)
years = years[1:]
# 获取每一列
trs = table_main.find_elements(By.XPATH, './tbody/tr')
dict_col = dict()
time.sleep(2)
# 得到每一列
for tr in trs:
    tds = tr.find_elements(By.XPATH, './td')
    # 一列中的每一行
    row = []
    for td in tds:
        row.append(td.text)

    # row[0]: 表头
    # row[1:]: 数据
    dict_col[row[0]] = row[1:]

# print(years)
# print(dict_col)

# 写入文件
dic = dict_col
# 表头
head = []
head.append("年份")
for i in dic.keys():
    head.append(i)
# 年末总人口
Total = dic['年末总人口(万人)']
# 男性人口
Male = dic['男性人口(万人)']
# 女性人口
Female = dic['女性人口(万人)']
# 城镇人口
Urban = dic['城镇人口(万人)']
# 乡村人口
Rural = dic['乡村人口(万人)']

with open("data/data.csv", "w") as f:
    csvf = csv.writer(f)
    # 写入表头
    csvf.writerow(head)
    data = []
    for i in range(len(Total)):
        data.append((years[i], Total[i], Male[i], Female[i], Urban[i], Rural[i]))
    csvf.writerows(data)
f.close()
