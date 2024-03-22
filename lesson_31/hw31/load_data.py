"""Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON and dump it to a file."""

import requests
from bs4 import BeautifulSoup

from robots import URL

writing = False

# response = requests.get(URL)
# soup = BeautifulSoup(response.text, "html.parser")
#
# text = soup.get_text()
#
# with open("wiki-text.txt", "w", encoding="utf-8") as file:
#     for line in text.split("\n"):
#         if "From Wikipedia, the free encyclopedia" in line:
#             writing = True
#
#         if writing:
#             file.write(line+"\n")

try:
    with requests.get(URL) as response:
        soup = BeautifulSoup(response.text, "html.parser")
except requests.RequestException:
    print("Request error")

content = soup.findAll("p")

with open("wiki-text.txt", "w", encoding="utf-8") as file:
    for p in content:
        file.write(p.get_text())



