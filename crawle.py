import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

class Crawler:
    def __init__(self, urls=[]):
        self.visited_urls = []
        self.urls_to_visit = urls
    def download_url(self, url):
        return requests.get(url).text
    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a',{"class":"card__link"}):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def add_url_to_visit(self, url):
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    def crawl(self, url):
        html = self.download_url(url)
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)

    def run(self):
        count=0
        path_w = r"D:\PY\NLP\data english\link1000page.txt"
        while self.urls_to_visit:
            count = count + 1
            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling {count}: {url}')
            with open(path_w,mode="a") as f:
                f.write(str(url)+"\n")
            if (count==1000) :
                break
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.visited_urls.append(url)
if __name__ == '__main__':
    page = 2
    while(page<63):
        Crawler(urls=['https://www.newscientist.com/section/news/page/'+str(page)+'/']).run()
        page = page+1