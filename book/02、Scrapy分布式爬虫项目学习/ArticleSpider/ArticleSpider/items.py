# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()  # 只能指定这个类型
    create_date = scrapy.Field()
    url = scrapy.Field()
    url_object_url = scrapy.Field()
    font_image_url = scrapy.Field()
    font_image_path = scrapy.Field()  # 本地存储路径
    praise_nums = scrapy.Field()
    comment_num = scrapy.Field()
    fav_nums = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()
