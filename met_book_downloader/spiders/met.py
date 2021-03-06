# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule, Spider
from met_book_downloader.items import BookItem
from scrapy.loader import ItemLoader
import re

class MetSpider(CrawlSpider):
    name = 'met'
    allowed_domains = ['metmuseum.org']
    start_urls = ['https://www.metmuseum.org/art/metpublications/all-available-titles/',]

    rules = (
        Rule(LinkExtractor(restrict_xpaths= [
            "//ul[@class='pagination']//li[@class='next']"
        ]), follow=True),

        Rule(LinkExtractor(restrict_xpaths= [
            "//*[@class='metpubs-result']//*[@class='metpubs-result-button-container']"
        ]), callback='parse_pew', follow=True)
    )

    def parse_pew(self, response):
        article = ItemLoader(item = BookItem(), response = response)
        # article.add_value('url', response.url)
        # article.add_xpath("book_title", '//div[@class="metpubs-title-container"]/text()', Join())
        # article.add_xpath("book_author", '//div[@class="metpubs-author-subcontainer"]/text()', Join())

        pdf_files = response.xpath('//a[@id="m_download_pdf_link"]/@onclick').extract()
        if len(pdf_files) > 0:
            path = re.findall('\(\'(.*)\'\)', str(pdf_files), re.DOTALL)

            item_file = ItemLoader(BookItem(), response = response)
            item_file.add_value('file_urls', path)
            item = item_file.load_item()
            yield(item)
        # yield {response.url : path}
