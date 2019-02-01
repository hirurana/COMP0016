# -*- coding: utf-8 -*-
import scrapy


class StandardSpider(scrapy.Spider):
    name = 'standard'
    allowed_domains = ['https://www.standard.co.uk/topic/coffee']
    start_urls = ['http://https://www.standard.co.uk/topic/coffee/']

    def parse(self, response):
        pass
