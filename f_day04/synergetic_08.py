#-*- codeing = utf-8 -*-
#@Time:2022/2/28 19:24
#@Author:王远辉
#@File:synergetic_08.py
#@Software:PyCharm

import asyncio

async def func():
    print("asdf")
if __name__ == '__main__':
    g = func() # 加上 async 关键字， 此时的函数是异步协程函数， 函数执行的结果返回的是一个协程对象
    # print(g)

    # 运行异步协程函数
    asyncio.run(g)




