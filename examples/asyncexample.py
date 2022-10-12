import asyncio
import xkcd


async def main():
    client = xkcd.AsyncClient()
    comic = await client.latest()
    print(comic.num)


asyncio.run(main())
