# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

from scrapy.pipelines.files import FilesPipeline
from scrapy.exceptions import DropItem

file_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'full')

class MetBookDownloaderPipeline(object):
    def process_item(self, item, spider):
        return item
