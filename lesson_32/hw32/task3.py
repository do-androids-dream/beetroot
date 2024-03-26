"""
Requests using multithreading

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON and dump it to a file. For this task use Threads for making requests to reddit API.
"""

import threading
import requests
import contextlib

from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Gandalf"


try:
    with requests.get(URL) as response:
        soup = BeautifulSoup(response.text, "html.parser")
except requests.RequestException:
    print("Request error")

content = soup.findAll("p")


def write_to_file(file, text, lock: threading.Lock):
    lock.acquire()
    file.write(text.get_text() + "\n")
    lock.release()


with open("wiki-text.txt", "w", encoding="utf-8") as file:
    lock = threading.Lock()
    threads = []
    for p in content:
        t = threading.Thread(target=write_to_file, args=(file, p, lock))
        threads.append(t)

    for t in threads:
        t.run()
