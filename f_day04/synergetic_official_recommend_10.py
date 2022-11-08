# -*- codeing = utf-8 -*-
# @Time:2022/2/28 19:54
# @Author:王远辉
# @File:synergetic_official_recommend_10.py
# @Software:PyCharm

# -*- codeing = utf-8 -*-
# @Time:2022/2/28 19:38
# @Author:王远辉
# @File:synergetic_09.py
# @Software:PyCharm
import time
import asyncio


async def func1():
    print("func1 start!")
    await asyncio.sleep(3)  # 异步操作的代码， 这样 协程才能生效
    print("func1 over!")


async def func2():
    print("func2 start!")
    await asyncio.sleep(3)
    print("func3 over!")


async def func3():
    print("func3 start!")
    await asyncio.sleep(4)
    print("func3 over!")


async def main():
    # 第一种写法
    # f1 = func1()
    # await f1
    # await func1()
    #      第二种写法（推荐）
    tasks = [func1(), func3(), func2()]
    tasks1 = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3()),
    ]
    await asyncio.wait(tasks1)
    '''
    注意： 过时警告：在python 3.8以后 不能将 异步协程任务 直接挂起，需要手动封装 task
        需要这样做：
        tasks1 = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3()),
    ]
    '''


if __name__ == '__main__':
    print("main start!")
    asyncio.run(main())
