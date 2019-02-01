# -*- coding: utf-8 -*-
import scrapy


class TheguardianSpider(scrapy.Spider):
    name = 'theguardian'
    allowed_domains = ['https://www.theguardian.com/food/coffee']
    start_urls = ['http://https://www.theguardian.com/food/coffee/']

    def parse(self, response):
        pass
