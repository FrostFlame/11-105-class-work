import asyncio

import aioconsole

msg = 'initial'


async def my_input():
    global msg
    while True:
        msg = await aioconsole.ainput()
        await asyncio.sleep(0.3)


async def my_print():
    while True:
        print(msg)
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(my_input(), my_print())


asyncio.run(main())
