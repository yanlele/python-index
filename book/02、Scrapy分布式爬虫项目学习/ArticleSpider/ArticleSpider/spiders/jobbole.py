# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com/']
    start_urls = ['http://blog.jobbole.com/113665/']

    def parse(self, response):
        re1_select = response.xpath('/html/body/div[1]/div[3]/div[1]/div[1]/h1')
        re2_select = response.xpath('//*[@id="post-113665"]/div[1]/h1')
        re3_select = response.xpath('//div[@class="entry-header"]/h1')
        pass
