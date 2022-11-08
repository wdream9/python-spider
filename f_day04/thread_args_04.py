#-*- codeing = utf-8 -*-
#@Time:2022/2/28 15:31
#@Author:王远辉
#@File:thread_args_04.py
#@Software:PyCharm

# 多线程进行传递参数
from threading import Thread

def func(name):
    for i in range(1000):
        print(name,i)
if __name__ == '__main__':
    t = Thread(target=func,args=("终结论",))
    t.start()
    t2 = Thread(target=func,args=("sadf",))
    t.start()