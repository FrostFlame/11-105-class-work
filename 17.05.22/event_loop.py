import asyncio


async def foo():
    await asyncio.sleep(5)
    print('foo')


async def bar():
    await asyncio.sleep(5)
    print('bar')


# async def main():
#     task1 = asyncio.create_task(foo())
#     task2 = asyncio.create_task(bar())
#     await asyncio.gather(task1, task2)
#     print('end')


# asyncio.run(main())


loop = asyncio.get_event_loop()
task1 = loop.create_task(foo())
task2 = loop.create_task(bar())
loop.run_until_complete(task1)
