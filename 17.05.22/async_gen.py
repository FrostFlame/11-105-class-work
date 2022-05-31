import asyncio
import time


async def ticker(delay, to):
    for i in range(to):
        yield (i, delay)
        await asyncio.sleep(delay)


async def run(k):
    async for i in ticker(k, 5):
        print(i)


async def main():
    await asyncio.gather(run(0.5), run(1))


if __name__ == '__main__':
    asyncio.run(main())
