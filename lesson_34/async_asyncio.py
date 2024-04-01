import requests

URL = "https://loremflickr.com/320/240/dog"


# def get_picture():
#     r = requests.get(URL, allow_redirects=True)
#     return r
#
#
# def save_picture(response: requests.Response):
#     file_name = response.url.split("/")[-1]
#     with open(file_name, "wb") as file:
#         file.write(response.content)
#
#
# def main():
#     for i in range(10):
#         pic = get_picture()
#         save_picture(pic)
#
#
# if __name__ == '__main__':
#     main()



#############################################################################################

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


