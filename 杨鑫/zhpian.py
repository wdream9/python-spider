#-*- codeing = utf-8 -*-
#@Time:2022/3/19 20:17
#@Author:王远辉
#@File:zhpian.py
#@Software:PyCharm


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
# options = Options()
# options.add_argument('ignore-certificate-errors')
# chrome = Chrome(options=options)
chrome = Chrome()
# chrome = Chrome()
chrome.get("https://www.xiaobaogong.com")
chrome.implicitly_wait(10)  # 隐式等待，等待页面加载完毕，直到页面加载完成，加载完成面就不等待了
# 点击登录
chrome.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/button').click()

# 跳过微信登录
chrome.find_element(By.XPATH, '//*[@id="app"]/div[16]/div/div[1]/button').click()

# 再次点击登录
chrome.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/button').click()
# 账号密码登录
chrome.find_element(By.XPATH, '//*[@id="app"]/div[16]/div/div[2]/div/div[3]/button').click()
# 账户
chrome.find_element(By.XPATH, '//*[@id="app"]/div[11]/div/div[2]/div/div[1]/div/input').send_keys("18285748638")
# 密码
chrome.find_element(By.XPATH, '//*[@id="app"]/div[11]/div/div[2]/div/div[2]/div/input').send_keys("Yx287758578")

# 登录
chrome.find_element(By.XPATH, '//*[@id="app"]/div[11]/div/div[2]/div/div[4]/div[1]/button').click()

print("sadf")
