import scrapy
from bs4 import BeautifulSoup
from ..items import PTTArticleItem
from pathlib import Path

class PttFirstSpider(scrapy.Spider):
    name = 'PTTFirst'
    
    def __init__(self, start_urls, filename=None):
        self.cookies = {'over18': '1'}
        self.start_urls = start_urls
        self.filename = filename
        super().__init__()
        
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookies)

    def parse(self, response):
        # 假設網頁回應不是 200 OK 的話, 我們視為傳送請求失敗
        if response.status != 200:
            print('Error - {} is not available to access'.format(response.url))
            return
        soup = BeautifulSoup(response.text)
        data = PTTArticleItem()
        for i in soup.find_all(class_='article-metaline'):
            data[i.find(class_='article-meta-tag').text] = i.find(class_='article-meta-value').text
            print(i.find(class_='article-meta-tag').text, ':',  i.find(class_='article-meta-value').text)
        
        data['context'] = soup.find(id='main-container').text.split('\n')
        print('\n====== text ======\n', soup.find(id='main-container').text.split('\n'))
        
        print('data: ', data)
        yield data
