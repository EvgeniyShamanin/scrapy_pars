# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from avitopars.items import AvitoparsItem


class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']
    start_urls = ['https://www.avito.ru/chelyabinsk/tovary_dlya_kompyutera?cd=1']

    def parse(self, response: HtmlResponse):
        last_page = response.xpath("//div[contains(@data-marker,'pagination-button')]/span[contains(@data-marker,"
                                   "'page')][last()]/text()").extract_first()
        items = response.xpath(
            "//div[@itemtype='http://schema.org/Product'] //a[@data-marker='item-title']/@href").extract()
        if int(last_page) > 1:
            count_page = int(last_page)
            while count_page > 1:
                page_url = f'https://www.avito.ru/chelyabinsk/tovary_dlya_kompyutera?cd=2&p={count_page}'
                count_page -= 1
                yield response.follow(page_url, callback=self.parse)
        for item in items:
            item_link = f'https://www.avito.ru/{item}'
            yield response.follow(item_link, callback=self.item_pars)

    def item_pars(self, response: HtmlResponse):
        name = response.xpath("//h1[@class='title-info-title']/span[@class='title-info-title-text']/text()").extract_first()
        price_dirty = response.xpath("//span[@itemprop='price']/@content").extract_first()
        yield AvitoparsItem(name=name, value=price_dirty)
