# -*- coding: utf-8 -*-
import scrapy


class TelegraphSpider(scrapy.Spider):
    name = 'telegraph'
    allowed_domains = ['https://www.telegraph.co.uk/coffee/']
    start_urls = ['http://https://www.telegraph.co.uk/coffee//']

    def parse(self, response):
        pass
