# -*- coding: utf-8 -*-
import scrapy


class JobboleCssSelecterSpider(scrapy.Spider):
    name = 'jobbole_css_selecter'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/110287/']

    def parse(self, response):
        title = response.css('div.entry-header h1::text').extract()[0]


        pass
