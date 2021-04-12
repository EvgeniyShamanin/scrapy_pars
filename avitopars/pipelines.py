# -*- coding: utf-8 -*-
from pymongo import MongoClient
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class AvitoparsPipeline:
    def process_item(self, item, spider):
        return item


class DataBasePipeline:
    def __init__(self):
        client = MongoClient('mongodb://localhost:27017/')
        self.mongo_base = client.avitoparse

    def process_item(self, item, spider):
        collection = self.mongo_base['avito']
        collection.update_one(item, {'$set': item}, upsert=True)
        return item
