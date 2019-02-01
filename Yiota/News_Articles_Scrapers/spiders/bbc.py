# -*- coding: utf-8 -*-
import scrapy


class BbcSpider(scrapy.Spider):
    name = 'bbc'
    allowed_domains = ['https://www.bbc.co.uk/news/topics/cdz5g8jnrjzt/coffee']
    start_urls = ['http://https://www.bbc.co.uk/news/topics/cdz5g8jnrjzt/coffee/']

    def parse(self, response):
        pass
