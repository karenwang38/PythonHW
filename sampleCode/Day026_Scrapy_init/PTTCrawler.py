# -*- coding: utf-8 -*-
import scrapy


class PttcrawlerSpider(scrapy.Spider):
    name = 'PTTCrawler'
    allowed_domains = ['https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html']
    start_urls = ['http://https://www.ptt.cc/bbs/Gossiping/M.1557928779.A.0C1.html/']

    def parse(self, response):
        pass
