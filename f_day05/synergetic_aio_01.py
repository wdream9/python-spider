# -*- codeing = utf-8 -*-
# @Time:2022/3/1 15:25
# @Author:王远辉
# @File:synergetic_aio_01.py
# @Software:PyCharm

# 安装 aiohttp ：pip install aiohttp
import asyncio
import aiohttp


urls = [
    "https://kr.zutuanla.com/file/2022/0223/4f198e37c544e1d67433fcbba9a38c1d.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/774218be86d832f359637ab120eba52d.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/1031/e9d17d27dfd693d88b232899538144e8.jpg"
]

async def download_img(url):

    '''
    发送请求: 在 异步协程函数当中不能使用原本的 requests 发送请求，
            需要使用我们 aiohttp 提供的api发送异步请求。
    '''
    name = url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # 请求回来，写入文件
            with open("img/" + name,mode="wb") as f:
                # 读取内容是异步的，需要 await 挂起
                f.write(await response.content.read())

async def main():
    # 创建 异步协程任务 列表
    task = []
    for url in urls:
        task.append(download_img(url))

    # 执行 异步协程任务
    # 若在异步协程函数种需要执行其他的阻塞操作那么 需要加上 await 关键字
    await asyncio.wait(task)

if __name__ == '__main__':
    asyncio.run(main())