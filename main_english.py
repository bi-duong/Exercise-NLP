from urllib.request import urlopen

from bs4 import BeautifulSoup
import requests
path=r"D:\PY\NLP\data english\link1000page.txt"
path_save = "D:/PY/NLP/data english/"
file_name="Bai bao thu "
i=768
with open(path, mode='r') as f:
    while True:
        data = f.readline()
        if data == '':
            break
        html = requests.get(data)
        i = i + 1
        soup = BeautifulSoup(html.text, "html.parser")
        h1 = soup.find("h1",{"class":"article__title"}).text

        div1 = soup.find("div", {"class": "article__content zephr-article-content"}).text
        print("Bai bao thu "+str(i))
        with open(path_save +file_name+ str(i)+".txt", mode='a',encoding="utf-8") as a:
            a.write(str(h1)+"\n"),
            #a.write( str(p1)+"\n"),
            a.write(str(div1)+"\n"),


    f.close()



