# -*- coding: utf-8 -*-
import scrapy


class MetroSpider(scrapy.Spider):
    name = 'metro'
    allowed_domains = ['https://metro.co.uk/tag/coffee/']
    start_urls = ['http://https://metro.co.uk/tag/coffee//']

    def parse(self, response):
        pass
