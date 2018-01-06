# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IsrablogItem(scrapy.Item):
    # define the fields for your item here like:
    nickname  = scrapy.Field()
    blogger_age= scrapy.Field()
    blogger_gender = scrapy.Field()
    post_title = scrapy.Field()
    post_content= scrapy.Field()
    post_date = scrapy.Field()
    post_hour= scrapy.Field()
    post_url =scrapy.Field()
    