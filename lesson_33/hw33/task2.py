"""
Requests using concurrent and multiprocessing libraries

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON and dump it to a file. For this task use concurrent and multiprocessing libraries for making requests to Reddit API.
"""

import threading
import multiprocessing
import requests
import concurrent.futures

from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Gandalf"


try:
    with requests.get(URL) as response:
        soup = BeautifulSoup(response.text, "html.parser")
except requests.RequestException:
    print("Request error")

content = soup.findAll("p")


def write_to_file(args):
    file, text = args
    file.write(text.get_text() + "\n")


if __name__ == '__main__':

    processes = []

    with open("wiki-text.txt", "w", encoding="utf-8") as file:
        # with concurrent.futures.ProcessPoolExecutor() as pool:
        #     pool.map(write_to_file, [(file, text) for text in content])

        for text in content:
            p = multiprocessing.Process(target=write_to_file, args=(file, text))
            processes.append(p)
            if len(processes) == 100:
                for p in processes:
                    p.run()
                    p.join()
            break
