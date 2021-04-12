# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class AvitoparsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    name = scrapy.Field()
    value = scrapy.Field()
    # id = scrapy.Field(output_processor=TakeFirst())
    # username = scrapy.Field(output_processor=TakeFirst())
    # profile_pic_url = scrapy.Field(output_processor=TakeFirst())
    # user_pars = scrapy.Field(output_processor=TakeFirst())
    # user_pars_id = scrapy.Field(output_processor=TakeFirst())
    # type = scrapy.Field(output_processor=TakeFirst())
