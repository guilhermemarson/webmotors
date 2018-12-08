# -*- coding: utf-8 -*-
import scrapy
from gather_urls.items import *


class UrlSpiderSpider(scrapy.Spider):
    name = 'url_spider'
    allowed_domains = ['webmotors.com.br']
    #urls = ['https://www.webmotors.com.br/carros/estoque']
    urls = ['https://www.webmotors.com.br/carros/estoque/citroen/c4']

    # Creates a list of urls to be scrapped
    start_urls = []

    for url in urls:
        for i in range(1, 2):
            start_urls.append(url + '?qt=36&o=1&p=' + str(i))

    def parse(self, response):
        qtd = response.xpath(
            '//*[@id="box-seo-count"]/span/text()').extract()[0].strip().split(' ')[0]

        qtd = qtd.replace('.', '')
        if int(qtd) % 36 == 0:
            count = int(qtd) / 36
        else:
            count = (int(qtd) // 36) + 1
        print(str(count))
        links = response.xpath('//a[@class="nn tipo1 c-after"]//@href').extract()
        for link in links:
            item=GatherUrlsItem()
            item['links']=link
            yield item
            
     #        yield link
        
        # for url in links:
     #        aux = GatherUrlsPipeline()
     #        print('############################################################################')
     #        print('############################################################################')
     #        print('############################################################################')
     #        print(aux)
     #        aux['links'] = url
     #        yield aux

