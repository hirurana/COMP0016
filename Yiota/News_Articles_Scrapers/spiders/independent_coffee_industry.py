# -*- coding: utf-8 -*-
import scrapy


class IndependentCoffeeIndustrySpider(scrapy.Spider):
    name = 'independent_coffee_industry'
    allowed_domains = ['https://www.independent.co.uk/topic/CoffeeIndustry']
    start_urls = ['http://https://www.independent.co.uk/topic/CoffeeIndustry/']

    def parse(self, response):
        pass
