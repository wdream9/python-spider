#-*- codeing = utf-8 -*-
#@Time:2022/2/28 15:06
#@Author:王远辉
#@File:thread_01.py
#@Software:PyCharm

# 导入线程类
from threading import Thread

def func():
    for i in range(10000):
        print(i)

if __name__ == '__main__':
    t = Thread(target=func())   # 创建线程并给线程安排任务  线程状态：新建态
    t.start() # 多线程状态： 就绪态
    for i in range(1000):
        print("main",i)
