from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from avitopars import settings
from avitopars.spiders.avito import AvitoSpider


if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(AvitoSpider)

    process.start()