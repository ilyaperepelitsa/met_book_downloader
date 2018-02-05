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
            "//*[@class='metpubs-result']//*[@class='next']"
        ]), callback='parse_pagination', follow=True),
    )

    def parse_pagination(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
