# pyxkcd

A simple, easy-to-use xkcd wrapper

-----

## Documentation

Coming soon™

## Quickstart

### Sync mode:

```py
import xkcd

client = xkcd.Client()

latest = client.latest()
print(latest.json())
```

### Async mode:

```py
import asyncio
import xkcd

client = xkcd.AsyncClient()

async def main():
    tasks = (client.random() for _ in range(25))
    return await asyncio.gather(*tasks)

asyncio.run(main())```
