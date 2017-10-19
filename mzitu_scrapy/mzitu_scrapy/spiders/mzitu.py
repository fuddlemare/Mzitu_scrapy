# -*- coding: utf-8 -*-

import scrapy

from mzitu_scrapy.mzitu_scrapy.items import MzituScrapyItem


class MzituSpider(scrapy.Spider):
    name = 'mzitu'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/all/']

    def parse(self, response):
        urls = response.xpath('//ul[@class="archives"]/li/p/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_image_url)

    def parse_image_url(self, respone):
        total_page = respone.xpath('//div[@class="content"]/div[@class="pagenavi"]/a[5]/span/text()').extract_first()
        for page in range(1, int(total_page) + 1):
            image_url = respone.url + '/' + str(page)
            yield scrapy.Request(image_url, callback=self.parse_image)

    def parse_image(self, response):
        image_url = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract_first()
        item = MzituScrapyItem()
        item['image_url'] = image_url
        item['image_referer_url'] = response.url
        yield item
