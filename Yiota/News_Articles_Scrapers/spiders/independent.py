# -*- coding: utf-8 -*-
import scrapy


class IndependentSpider(scrapy.Spider):
    name = 'independent'
    allowed_domains = ['https://www.independent.co.uk/topic/Coffee']
    start_urls = ['http://https://www.independent.co.uk/topic/Coffee/']

    def parse(self, response):
        pass
