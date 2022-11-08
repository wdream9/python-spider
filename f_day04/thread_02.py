#-*- codeing = utf-8 -*-
#@Time:2022/2/28 15:16
#@Author:王远辉
#@File:thread_02.py
#@Software:PyCharm

from threading import Thread

# 类之间的继承
class MyThread(Thread):
    def run(self):
        for i in range(10000):
            print("mythread",i)

if __name__ == '__main__':
    t = MyThread() # 创建一个对象，就像java中继承thread类，然后new 一个新的对象
    t.start()   #  通过 调用Thread类的start方法开启线程，  注意 t.run 只是类方法的调用

    for i in range(1000):
        print("main",i)

#     控制台输出部分结果如下
# mythread535
#  549
# mythreadmain 536
#  550
# mythreadmain  551
# mythread537
# main  552
# mythread538