# -*- codeing = utf-8 -*-
# @Time:2022/2/28 19:38
# @Author:王远辉
# @File:synergetic_09.py
# @Software:PyCharm
import time
import asyncio


async def func1():
    print("func1 start!")
    # time.sleep(3)  # 当程序出现了同步操作时，异步就中断了
    await asyncio.sleep(3)  #异步操作的代码， 这样 协程才能生效
    print("func1 over!")


async def func2():
    print("func2 start!")
    await asyncio.sleep(3)
    # time.sleep(2)
    print("func3 over!")


async def func3():
    print("func3 start!")
    # time.sleep(4)
    await asyncio.sleep(4)
    print("func3 over!")


if __name__ == '__main__':
    print("main start==========>")
    f1 = func1()
    f2 = func2()
    f3 = func3()

    tasks = [f1, f2, f3]

    t1 = time.time()  # 获取时间戳

    # 执行一个  异步 协程 函数
    # asyncio.run(g)
    # 一次性执行多个异步任务
    asyncio.run(asyncio.wait(tasks))
    t2 = time.time()
    print(t2 - t1)
