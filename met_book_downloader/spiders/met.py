# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MetSpider(CrawlSpider):
    name = 'met'
    allowed_domains = ['metmuseum.org']
    start_urls = ['https://www.metmuseum.org/art/metpublications/all-available-titles']

    rules = (
        Rule(LinkExtractor(restrict_xpaths= [
            "//*[@class='pagination']//li[@class='next']"
        ]), follow=True),

        Rule(LinkExtractor(restrict_xpaths= [
            "//*[@class='metpubs-result']//*[@class='metpubs-result-button-container']"
        ]), callback='parse_book', follow=True),
    )

    def parse_book(self, response):
        article = ItemLoader(item = BookItem(), response = response)
        article.add_value('url', response.url)
        article.add_xpath("article_text", '//div[@class=""]/p/text()', Join())
        article.add_xpath("article_title", '//h1/text()', Join())
        article.add_xpath("author_name", '//div[@class = "byline"]/a[@rel="author"]/text()')
        article.add_xpath("date_published", '//meta[@name = "sailthru.date"]/@content', Join())

        item = article.load_item()
        return i
