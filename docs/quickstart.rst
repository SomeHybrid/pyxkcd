Quickstart
==========

A minimal example showcasing the pyxkcd API.

Sync example
--------------

.. code:: python3

    import xkcd
    client = xkcd.Client()
    
    # Get the latest comic
    comic = client.latest()

    # Get the comic number:
    print(comic.num)


Async example
-------------

.. code:: python3

    import asyncio
    import xkcd
    
    async def main():
        client = xkcd.AsyncClient()
        comic = await client.latest()
        print(comic.num)
    
    asyncio.run(main())


There are also more examples in the :repository:`\ `.