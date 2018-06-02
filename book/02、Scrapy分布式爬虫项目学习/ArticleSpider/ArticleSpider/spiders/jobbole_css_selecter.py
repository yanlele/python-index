# -*- coding: utf-8 -*-
import re
import scrapy


class JobboleCssSelecterSpider(scrapy.Spider):
    name = 'jobbole_css_selecter'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/110287/']

    def parse(self, response):
        # title
        title = response.css('div.entry-header h1::text').extract()[0]

        # 创建日期
        create_date = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().strip().replace('·', '').strip()

        # 点赞数
        praise_nums = response.css("span.vote-post-up h10::text").extract()[0]

        # 收藏数
        fav_nums = response.css("span.bookmark-btn::text").extract()[0]
        match_re = re.match('.*(\d+).*', fav_nums)
        if match_re:
            fav_nums = match_re.group(1)
        else:
            fav_nums = 0

        # 评论数


        pass
