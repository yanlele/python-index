# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http import Request
from urllib import parse


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com/']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        1、获取文章列表页面的具体文章url并交给scrapy下载，然后交给解析函数进行具体字段的解析
        2、获取下一页的url 并交给scrapy进行下载，下载完成之后交给parse函数
        :param response:
        :return:
        """
        # 解析列表页中的所有文章url并交给scrapy下载后并进行解析
        post_urls = response.css("#archive div.floated-thumb div.post-thumb a::attr(href)").extract()
        for post_url in post_urls:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail) # 如果没有完整的url的时候，这个时候我们可以利用parse.urljoin(base_url, url)来拼接
            # yield Request(url=post_url, callback=self.parse_detail)

        # 提取下一页交给 scrapy 来进行下载
        next_urls = response.css('a.next.page-numbers::attr(href)').extract_first("")
        if next_urls:
            yield Request(url=next_urls, callback=self)



    def parse_detail(self, response):
        # 提取文章的具体字段

        # 获取文章的title
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]

        # 获取文章的创建时间
        create_time = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace('·', '').strip()

        # 获取文章的点赞数
        praise_nums = int(response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0])

        # 收藏数量
        fav_nums = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
        match_re = re.match('.*?(\d+).*', fav_nums)
        if match_re:
            fav_nums = match_re.group(1)
        else:
            fav_nums = 0

        # 评论数
        comment_num = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        match_re = re.match('.*?(\d+).*', comment_num)
        if match_re:
            comment_num = match_re.group(1)
        else:
            comment_num = 0

        # 获取文章正文 - 这个地方我们可以直接把html字符串提取出来就完了
        content = response.xpath("//div[@class='entry']").extract()[0]

        # 获取文章关键字
        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ','.join(tag_list)

        pass
