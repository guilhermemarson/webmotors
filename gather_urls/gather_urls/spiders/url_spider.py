# -*- coding: utf-8 -*-
import scrapy


class UrlSpiderSpider(scrapy.Spider):
    name = 'url_spider'
    allowed_domains = ['webmotors.com.br']
    #urls = ['https://www.webmotors.com.br/carros/estoque']
    urls=['https://www.webmotors.com.br/carros/estoque/citroen/c4']

	# Creates a list of urls to be scrapped
    start_urls = []

    for url in urls:        
        for i in range(1, 2):
            start_urls.append(url + '?qt=36&o=1&p=' + str(i))


    def parse(self, response):
    	qtd = response.xpath('//*[@id="box-seo-count"]/span/text()').extract()[0].strip().split(' ')[0]
    	print('############################################################################')
    	print('############################################################################')
    	print('############################################################################')
    	#print(qtd[0].strip().split(' ')[0])
    	print(qtd)
        # with open("test.html", 'wb') as file:
        #     file.write(response.body)
