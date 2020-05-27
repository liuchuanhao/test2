# -*- coding: utf-8 -*-
import asyncio
import random


async def corn_scheduler():
    page = 1
    while True:
        # await asyncio.sleep(1)
        job = cron_job("{}/{}".format("https://www.baidu.com",page))#直接交给eventloop
        page += 1
        # await job
        asyncio.run(job)
        # asyncio.create_task(job)#注册事件循环
        # await asyncio.gather([job,])
        await asyncio.sleep(0) #主动让出线程


async def cron_job(url):
    #模拟延迟
    n = random.randint(1,3)
    await asyncio.sleep(n)
    print("下载结束",url)

co = corn_scheduler()
loop = asyncio.get_event_loop()
loop.run_until_complete(co)



