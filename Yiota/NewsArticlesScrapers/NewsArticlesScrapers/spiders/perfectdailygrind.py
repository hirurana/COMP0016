# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime, timedelta

from NewsArticlesScrapers.items import NewsItem

class PerfectdailygrindSpider(scrapy.Spider):

    name = "perfectdailygrind"

    def start_requests(self):
        start_date = datetime(2014, 11, 25)

        date = start_date
        while date <= datetime.now():
            new_request = scrapy.Request(self.generate_url(date))
            new_request.meta["date"] = date
            new_request.meta["page_number"] = 1
            yield new_request
            date += timedelta(days=1)

    def generate_url(self, date, page_number=None):
        url = 'https://www.perfectdailygrind.com/' + date.strftime("%Y/%m/%d") + "/"
        if page_number:
            url  += "page/" + str(page_number) + "/"
        return url

    def parse(self, response):
        date = response.meta['date']
        page_number = response.meta['page_number']

        if response.status == 200:
            articles = response.xpath('//*[@id="off-canvas-body"]/div[4]/div/div/div/div[1]/div/div[3]/div/div/h3/a/@href').extract()
            for url in articles:
                request = scrapy.Request(url,
                                callback=self.parse_article)
                request.meta['date'] = date
                yield request

            url = self.generate_url(date, page_number+1)
            request = scrapy.Request(url,
                            callback=self.parse)
            request.meta['date'] = date
            request.meta['page_number'] = page_number
            yield request

    def parse_article(self, response):
        item = NewsItem()
        item['title'] = response.xpath('//*[@id="off-canvas-body"]/div[4]/div/div/div[1]/div/div/div[2]/div/div/div/h1/text()').extract()
        item['text'] = response.xpath('//div[@class="pf-content"]//text()').extract()
        item['date'] = str(response.meta['date'])
        item['url'] = response.url
        item['source'] = "perfectdailygrind.com"
        yield item
