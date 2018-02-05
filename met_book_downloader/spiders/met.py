# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule, Spider
from met_book_downloader.items import BookItem
from scrapy.loader import ItemLoader
import re

class MetSpider(Spider):
    name = 'met'
    allowed_domains = ['metmuseum.org']
    start_urls = ['https://www.metmuseum.org/art/metpublications/all-available-titles']

    rules = (
        Rule(LinkExtractor(restrict_xpaths= [
            "//*[@class='pagination']//li[@class='next']"
        ]), follow=True),

        Rule(LinkExtractor(restrict_xpaths= [
            "//*[@class='metpubs-result']//*[@class='metpubs-result-button-container']"
        ]), callback='parse', follow=True),
    )

    def parse_book(self, response):
        article = ItemLoader(item = BookItem(), response = response)
        # article.add_value('url', response.url)
        # article.add_xpath("book_title", '//div[@class="metpubs-title-container"]/text()', Join())
        # article.add_xpath("book_author", '//div[@class="metpubs-author-subcontainer"]/text()', Join())

        pdf_files = response.xpath('//a[@id="m_download_pdf_link"]/@onclick').extract()
        path = "".join(re.findall('\(\'(.*)\'\)', pewpew, re.DOTALL))

        item_file = ItemLoader(BookItem(), response = response)
        item_file.add_value('file_urls', str(path))
        item = item_file.load_item()
        yield(item)
