# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PTTArticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    作者 = scrapy.Field()
    標題 = scrapy.Field()
    時間 = scrapy.Field()
    context = scrapy.Field()
