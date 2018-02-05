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
        file_url = item['file_urls'][0]
        filename = file_url.split("/")[-1].replace("_", " ")
        cur_file = item['files'][0]['path'].split('/')[-1]
        file_path = os.path.join(file_dir, cur_file)
        os.rename(file_path, os.path.join(file_dir, filename))

        item["file_urls"] = item["file_urls"]
        item["files"] = item["files"][0]
        return item
