# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http import Request
from urllib import parse

from ArticleSpider.items import JobBoleArticleItem


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com/']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    headers = {
        "HOST": "blog.jobbole.com",
        "Referer": "http://blog.jobbole.com/all-posts/",
    }



    def parse(self, response):
        """
        1、获取文章列表页面的具体文章url并交给scrapy下载，然后交给解析函数进行具体字段的解析
        2、获取下一页的url 并交给scrapy进行下载，下载完成之后交给parse函数
        """
        # 解析列表页中的所有文章url并交给scrapy下载后并进行解析
        post_nodes = response.css("#archive div.floated-thumb .post-thumb a")
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            url = parse.urljoin(response.url, post_url)         # 这个会自动帮我们拼接我们想要的url地址： parse.urljoin(base_url, url)
            yield Request(url=url, callback=self.parse_detail, headers=self.headers, meta={"front_image_url": image_url}, dont_filter=True)

        # 提取下一页交给 scrapy 来进行下载
        next_urls = response.css('a.next.page-numbers::attr(href)').extract_first("")
        if next_urls:
            yield Request(url=parse.urljoin(response.url, next_urls), headers=self.headers, callback=self.parse)

    def parse_detail(self, response):
        """
        提取文章的具体字段
        :param response:
        :return:
        """

        # 实例化接受对象
        article_item = JobBoleArticleItem()

        # 获取title的图片(封面图) 这个地方我们可以通过字典的方式来查找，也可以通过get的方式来查找，建议get方式，这样不会出现异常
        font_image_url = response.meta.get("front_image_url", "")

        # 获取文章的title
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first()

        # 获取文章的创建时间
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace('·', '').strip()

        # 获取文章的点赞数
        praise_nums = int(response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0])

        # 收藏数量
        fav_nums = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
        match_re = re.match('.*?(\d+).*', fav_nums)
        if match_re:
            fav_nums = int(match_re.group(1))
        else:
            fav_nums = 0

        # 评论数
        comment_num = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        match_re = re.match('.*?(\d+).*', comment_num)
        if match_re:
            comment_num = int(match_re.group(1))
        else:
            comment_num = 0

        # 获取文章正文 - 这个地方我们可以直接把html字符串提取出来就完了
        content = response.xpath("//div[@class='entry']").extract()[0]

        # 获取文章关键字
        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ','.join(tag_list)

        # 填充article_item
        article_item["title"] = title
        article_item["url"] = response.url
        article_item["create_date"] = create_date
        article_item["font_image_url"] = font_image_url
        article_item["praise_nums"] = praise_nums
        article_item["comment_num"] = comment_num
        article_item["fav_nums"] = fav_nums
        article_item["tags"] = tags
        article_item["content"] = content

        # 传递到pipelines.py
        yield article_item
