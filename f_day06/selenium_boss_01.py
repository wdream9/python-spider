# -*- codeing = utf-8 -*-
# @Time:2022/3/2 12:10
# @Author:王远辉
# @File:selenium_boss_01.py
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

# chrome = Chrome(options=options)
chrome = Chrome()
chrome.maximize_window()
chrome.get("https://passport.kaikeba.com/login?redirect=https%3A%2F%2Flearn.kaikeba.com%2Ftransfer&app=learn&appid=hky8475638475664&sourceId=12000&callerId=3")
chrome.implicitly_wait(10)  # 隐式等待，等待页面加载完毕，直到页面加载完成，加载完成面就不等待了
# 获取职位输入框
chrome.find_element(By.XPATH, '//*[@id="filter-box"]/div/div[1]/div[1]/form/div[1]/p/input').send_keys("python",
                                                                                                       Keys.ENTER)
# 不等带页面数据加载完成直接去解析数据，就会出现找不到元素，解析失败

# 解析方法：css或者 xpath
# 第一步：就是获取所有的 li 元素标签
# lis = chrome.find_elements_by_xpath('//*[@id="main"]/div/div[3]/ul/li') # 过时
# lis = chrome.find_elements_by_css_selector(".job-tab li")      # 过时
# for li in lis:
#     print(li)

# 第一个岗位
li = chrome.find_element(By.XPATH, './/*[@id="main"]/div/div[3]/ul/li[1]')
lis = chrome.find_elements(By.XPATH, './/*[@id="main"]/div/div[3]/ul/li')
# 获取职位名称
post_name = li.find_element(By.XPATH, './div/div[1]/div[1]/div/div[1]/span[1]/a')
# 公司名称
company = li.find_element(By.XPATH, './div/div[1]/div[2]/div/h3/a')
#  工作地址
address = li.find_element(By.XPATH, './div/div[1]/div[1]/div/div[1]/span[2]/span')
# 薪资
pay = li.find_element(By.XPATH, './div/div[1]/div[1]/div/div[2]/span')
# 岗位学历要求
education = li.find_element(By.XPATH, './div/div[1]/div[1]/div/div[2]/p')
# 技能要求
skill_list = []
skills = li.find_elements(By.XPATH, './div/div[2]/div[1]/span')
for skill in skills:
    if skill.text != '':
        skill_list.append(skill.text)

# 打开一个文件
# 我的电脑：如果设置编码为 utf-8 idea中打开正常，不设置则乱码，在idea外面打开不会乱码
f = open("data/boss.csv", mode="w",encoding="utf-8")
# 表头
dic = {
    "岗位": post_name.text,
    "公司": company.text,
    "地址": address.text,
    "薪资": pay.text,
    "学历/经验": education.text,
    "技能": skill_list
}
csv_write = csv.DictWriter(f, fieldnames=[
    "岗位",
    "公司",
    "地址",
    "薪资",
    "学历/经验",
    "技能"
])
# 写入表头
csv_write.writeheader()
csv_write.writerow(dic)
# 输出
print(post_name.text, company.text, address.text, pay.text, education.text, list(skill_list))
# print(lis)
