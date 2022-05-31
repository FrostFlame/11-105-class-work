import asyncio


class MyIter:
    def __init__(self, delay):
        self.delay = delay


    def __aiter__(self):
        return self

    async def __anext__(self):
        while True:
            await asyncio.sleep(self.delay)
            return 'n' + str(self.delay)
        raise StopAsyncIteration


async def foo(delay):
    async for i in MyIter(delay):
        print(i)


async def main():
    await asyncio.gather(foo(0.5), foo(1))

asyncio.run(main())
