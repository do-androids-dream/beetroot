"""
Requests using asyncio and aiohttp

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON and dump them to a file. For this task use asyncio and aiohttp libraries for making requests to Reddit API.
"""

import asyncio
import aiohttp

URL = "https://loremflickr.com/320/240/dog"


def save_picture(picture: aiohttp.ClientResponse.content, file_name):

    with open(file_name, "wb") as file:
        file.write(picture)


async def get_picture(session: aiohttp.ClientSession):
    async with session.get(URL, allow_redirects=True) as response:
        pic = await response.read()
        file_name = str(response.url).split("/")[-1]
        print(file_name)
        save_picture(pic, file_name)


async def main():
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(get_picture(session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
