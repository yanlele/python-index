# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json
import MySQLdb
import MySQLdb.cursors
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWithEncodingPipeline(object):
    # 自定义json文件的导出
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding="utf-8")

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


class MysqlPipeline(object):
    """采用同步的方式写入数据"""
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', '53693750', '0001_article_spider', charset="utf8",
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # jobbole_article
        insert_sql = """
            insert into jobbole_article(title, create_date, url, url_object_id, font_image_url, font_image_path, praise_nums, comment_num, fav_nums, tags, content)
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql, (item["title"], item["create_date"], item["url"], item["url_object_id"],
                                         item["font_image_url"], item["font_image_path"], item["praise_nums"],
                                         item["comment_num"], item["fav_nums"], item["tags"], item["content"]))
        self.conn.commit()


class MysqlTwistedPipeline(object):
    """采用异步的方式写入数据"""
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"],
            db=settings["MYSQL_DBNAME"],
            user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted, 将mysql插入变为异步操作
        # jobbole_article
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)  # 处理异常

    def handle_error(self, failure, item, spider):
        # 处理异步插入的异常
        print(failure)

    def do_insert(self, cursor, item):
        # 这里实现具体的插入逻辑
        insert_sql = """
                    insert into jobbole_article(title, create_date, url, url_object_id, font_image_url, font_image_path, praise_nums, comment_num, fav_nums, tags, content)
                    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
        cursor.execute(insert_sql, (item["title"], item["create_date"], item["url"], item["url_object_id"],
                                    item["font_image_url"], item["font_image_path"], item["praise_nums"],
                                    item["comment_num"], item["fav_nums"], item["tags"], item["content"]))


class JsonExporterPipeline(object):
    # 调用scrapy提供的json export到处json文件
    def __init__(self):
        self.file = open('articleExport.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        # 我们可以通过results 来获取到文件的实际存储路径
        for ok, value in results:
            image_file_path = value["path"]
        item["font_image_path"] = image_file_path

        return item
