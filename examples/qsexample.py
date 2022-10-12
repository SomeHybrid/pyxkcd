import xkcd

client = xkcd.Client()

# Get the latest comic
comic = client.latest()

# Get the comic number:
print(comic.num)
