#-*- codeing = utf-8 -*-
#@Time:2022/2/28 19:11
#@Author:王远辉
#@File:Synergetic_07.py
#@Software:PyCharm

import time

def func():
    print("1")
    time.sleep(3)    # 让当前线程处于阻塞状态，cpu不为我工作
    print("2")

if __name__ == '__main__':
    func()

# input() ：程序也是处于阻塞状态
# requests.get(): 程序也是处于阻塞状态

# 一般情况下，程序处于IO状态时，线程程序是处于阻塞状态。

# 协程：为了实现 IO 时不放弃cpu的执行权，协程  就是这样干事的 ，可以选择性的切换到其他工作。
# 在微观上是一个任务一个任务的切换，切换的条件一般就是IO操作。
# 在宏观上，我们能看到的其实是多个任务在一起执行。

# 上方所讲一切都是在单线程的条件下。
# 任务的切换是由线程决定了



