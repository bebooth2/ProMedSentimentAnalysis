# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DocreviewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    doctor = scrapy.Field()
    review = scrapy.Field()
   
