#-*- codeing = utf-8 -*-
#@Time:2022/2/28 15:26
#@Author:王远辉
#@File:process_03.py
#@Software:PyCharm

# 多进程

from multiprocessing import Process

def func():
    for i in range(2000):
        print(i)

if __name__ == '__main__':
    p = Process(target=func())
    p.start()

    # for i in range(1000):
    #     print("main",i)
