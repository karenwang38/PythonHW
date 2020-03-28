import scrapy
from bs4 import BeautifulSoup
from ..items import PTTArticleItem
from pathlib import Path
from urllib.parse import urljoin, urlparse

class PttFirstSpider(scrapy.Spider):
    name = 'PTTFirst'
    
    def __init__(self, board='Gossiping'):
        self.cookies = {'over18': '1'}
        self.host = 'https://www.ptt.cc'
        self.board = board
        self.start_urls = 'https://www.ptt.cc/bbs/{}/index.html'.format(board)
        super().__init__()
        
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls, callback=self.parse, cookies=self.cookies)
    
    def parse(self, response):
        # 取得列表中的清單主體
        soup = BeautifulSoup(response.text)
        main_list = soup.find('div', class_='bbs-screen')

        # 依序檢查文章列表中的 tag, 遇到分隔線就結束，忽略這之後的文章
        for div in main_list.findChildren('div', recursive=False):
            class_name = div.attrs['class']

            # 遇到分隔線要處理的情況
            if class_name and 'r-list-sep' in class_name:
                self.log('Reach the last article')
                break

            # 遇到目標文章
            if class_name and 'r-ent' in class_name:
                div_title = div.find('div', class_='title')
                a_title = div_title.find('a', href=True)
                # 如果文章已經被刪除則跳過
                if not a_title or not a_title.has_attr('href'):
                    continue
                article_URL = urljoin(self.host, a_title['href'])
                article_title = a_title.text
                self.log('Parse article {}'.format(article_title))
                yield scrapy.Request(url=article_URL,
                                     callback=self.parse_article,
                                     cookies=self.cookies)

    def parse_article(self, response):
        # 假設網頁回應不是 200 OK 的話, 我們視為傳送請求失敗
        if response.status != 200:
            print('Error - {} is not available to access'.format(response.url))
            return
        soup = BeautifulSoup(response.text)
        data = PTTArticleItem()
        data['url'] = response.url
        for i in soup.find_all(class_='article-metaline'):
            data[i.find(class_='article-meta-tag').text] = i.find(class_='article-meta-value').text
            print(i.find(class_='article-meta-tag').text, ':',  i.find(class_='article-meta-value').text)
        
        data['context'] = soup.find(id='main-container').text.split('\n')
        print('\n====== text ======\n', soup.find(id='main-container').text.split('\n'))
        
        print('data: ', data)
        yield data
