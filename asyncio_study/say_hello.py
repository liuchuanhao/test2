# -*- coding: utf-8 -*-
import asyncio

async def sleep():
    i = 1
    while True:
        print("helloworld", i)
        i += 1
        await asyncio.sleep(1)

async def print_goodbye():
    while True:
        print("good bye")
        await asyncio.sleep(2)


# 创建携程对象
co1 = sleep()
co2 = print_goodbye()

# 获取事件循环
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(co1, co2))


