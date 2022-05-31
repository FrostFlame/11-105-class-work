import asyncio
from itertools import cycle

import aioconsole

array = []

async def foo():
    msg = await aioconsole.ainput()
    array.append(msg)
    # await asyncio.sleep(0.3)


async def bar():
    while True:
        if array:
            print[array.pop(0)]
        await asyncio.sleep(3)


x = ['5', '4']
for i in cycle(x):
    print(i)
