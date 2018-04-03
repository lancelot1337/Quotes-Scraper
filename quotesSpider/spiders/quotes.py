# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        
    	#Only first page scraping
        #h1Tag = response.xpath('//h1/a/text()').extract_first()
        #popTags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        #yield {'H1 Tag' : h1Tag, 'Popular Tags' : popTags}
        quotes = response.xpath('//*[@class="quote"]')
        
        for quote in quotes:
        	text = quote.xpath('.//*[@class="text"]/text()').extract_first()
        	author = quote.xpath('.//*[@class="author"]/text()').extract_first()
        	tags = quote.xpath('.//*[@class="keywords"]/@content').extract_first()
       		yield{'Text' : text, 'Author' : author, 'Tags' : tags } 
       	
       	nextPageURL = response.xpath('//*[@class="next"]/a/@href').extract_first()
       	absoluteNextPageURL = response.urljoin(nextPageURL)
       	yield scrapy.Request(absoluteNextPageURL)