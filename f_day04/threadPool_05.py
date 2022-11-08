#-*- codeing = utf-8 -*-
#@Time:2022/2/28 15:39
#@Author:王远辉
#@File:threadPool_05.py
#@Software:PyCharm

# 线程池： 一次性开辟一些线程，我们用户直接给线程池提交任务，线程任务的调度交给线程池来完成。
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
def func(name):
    for i in range(1000):
        print(name,i)
# /html/body/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div[1]/p[2]/span

if __name__ == '__main__':
    # 创建线程池
    with ThreadPoolExecutor(50) as pool:
        for i in range(100):
            # 提交任务到线程池
            pool.submit(func,name = f"线程{i}")

    print("over!")