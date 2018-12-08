# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import unicodecsv as csv
from datetime import date
from scrapy.exporters import CsvItemExporter


class GatherUrlsPipeline(object):
    # def __init__(self):
    #     if not os.path.isfile('webmotors_urls.csv'):
    #         self.csvwriter = csv.writer(open('webmotors_urls.csv', 'a'), delimiter=';', encoding='utf-8')           
            
    #         #self.csvwriter.writerow(['LINKS'])
    #     else:
    #         self.csvwriter = csv.writer(open('webmotors_urls.csv', 'a'), delimiter=';', encoding='utf-8')

    def process_item(self, item, spider):
        print('&&&&&&&&&&&&&&&&&&&&&&')
        print('&&&&&&&&&&&&&&&&&&&&&&')
        print('&&&&&&&&&&&&&&&&&&&&&&')
        print('&&&&&&&&&&&&&&&&&&&&&&')
        print('&&&&&&&&&&&&&&&&&&&&&&')
        # print(items['links'])
        # self.csvwriter.writerow([item['links']])
        file = open('webmotors_urls.csv','w+b')
        #self.files[spider] = file
        self.export_fields = ['links']
        self.exporter = CsvItemExporter(file, fields_to_export=self.export_fields)
        self.exporter.start_exporting()
        self.exporter.export_item(item)
        return item
