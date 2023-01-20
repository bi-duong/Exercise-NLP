import re
import urllib
import requests
path = r"D:\Natural Language Processing\Text representation 3\test.txt"

from bs4 import BeautifulSoup
with open(path, mode='r') as f:
    while True:
        data = f.readline()
        if data == '':
            break
        html =requests.get(data)
        soup = BeautifulSoup(html.text, "html.parser")
        div = soup.find("div", {"class": "title-top"})
        content=div.text
        print(content)
    f.close()