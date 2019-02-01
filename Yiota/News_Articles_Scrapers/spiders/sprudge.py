# -*- coding: utf-8 -*-
import scrapy


class SprudgeSpider(scrapy.Spider):
    name = 'sprudge'
    allowed_domains = ['https://sprudge.com/category/wire']
    start_urls = ['http://https://sprudge.com/category/wire/']

    def parse(self, response):
        pass
