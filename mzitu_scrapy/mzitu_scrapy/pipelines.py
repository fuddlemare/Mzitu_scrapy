# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import scrapy

from mzitu_scrapy.mzitu_scrapy import headers


class SaveImageToLocalPipeline(object):
    def process_item(self, item, spider):
        image_url = item['image_url']
        image_referer_url = item['image_referer_url']
        image_name = image_url[21:].replace('/', '')
        # image = scrapy.Request(image_url, headers=headers.Headers().get_headers(image_referer_url))
        with open('images/' + image_name, 'wb') as f:
            response = requests.get(image_url, headers=headers.Headers().get_headers(image_referer_url))
            f.write(response.content)
            f.close()
