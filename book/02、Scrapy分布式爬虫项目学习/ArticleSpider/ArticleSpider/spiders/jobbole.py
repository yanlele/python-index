# -*- coding: utf-8 -*-
import re
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com/']
    start_urls = ['http://blog.jobbole.com/113665/']

    def parse(self, response):
        re1_select = response.xpath('/html/body/div[1]/div[3]/div[1]/div[1]/h1')
        re2_select = response.xpath('//*[@id="post-113665"]/div[1]/h1')

        # 获取文章的title
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]

        # 获取文章的创建时间
        create_time = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace('·', '').strip()

        # 获取文章的点赞数
        praise_nums = int(response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0])

        # 收藏数量
        fav_nums = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
        match_re = re.match('.*(\d+).*', fav_nums)
        if match_re:
            fav_nums = match_re.group(1)
        else:
            fav_nums = 0

        # 评论数
        comment_num = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        match_re = re.match('.*(\d+).*', comment_num)
        if match_re:
            comment_num = match_re.group(1)
        else:
            comment_num = 0

        pass
