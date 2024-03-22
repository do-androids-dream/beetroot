import requests
from html import parser

"""Download and save to file robots.txt from wikipedia, twitter websites etc."""

URL = "https://en.wikipedia.org/wiki/Gandalf"

if __name__ == '__main__':
    response = requests.get(URL)
    print(response.status_code)
    print(response.headers, end="\n\n")
    print(response.text, end="\n\n")
    html = response.content.decode()

    with open("robots.txt", "w", encoding="utf-8") as file:
        file.write(html)
