import asyncio


async def foo():
    print('foo')


async def bar():
    print('bar')


async def main():
    await asyncio.gather(foo(), bar())


asyncio.run(main())
