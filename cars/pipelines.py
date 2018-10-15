# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from scrapy import log

import pymysql
from scrapy.utils.project import get_project_settings
from twisted.enterprise import adbapi


class JsonWithEncodingPipeline(object):
    """保存到文件中对应的class
           1、在settings.py文件中配置
           2、在自己实现的爬虫类中yield item,会自动执行"""

    def __init__(self):
        self.file = codecs.open('info.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"  # 转为json的
        self.file.write(line)  # 写入文件中
        return item

    def spider_closed(self, spider):  # 爬虫结束时关闭文件
        self.file.close()


class WebcrawlerScrapyPipeline(object):
    """保存到数据库中对应的class
           1、在settings.py文件中配置
           2、在自己实现的爬虫类中yield item,会自动执行"""

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparams = dict(host=settings['MYSQL_HOST'],  # 读取settings中的配置
                        db=settings['MYSQL_DBNAME'],
                        user=settings['MYSQL_USER'],
                        passwd=settings['MYSQL_PASSWD'],
                        charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
                        cursorclass=pymysql.cursors.DictCursor,
                        use_unicode=False, )
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._insert_item, item)
        query.addErrback(self.handle_error, item, spider)
        return item

    def _insert_item(self, cursor, item):
        sql, params = item.distinct_data()
        cursor.execute(sql, params)
        data = cursor.fetchone()
        if data:
            pass
        else:
            sql, params = item.get_insert_sql()
            cursor.execute(sql, params)
            cursor.commit()

    def handle_error(self, error, item, spider):
        print("*" * 10 + "error")
        print(error)


class ScrapyMySQLPipeline(object):
    def __init__(self):
        self.settings = get_project_settings()
        self.host = self.settings['MYSQL_HOST']
        self.port = self.settings['MYSQL_PORT']
        self.user = self.settings['MYSQL_USER']
        self.passwd = self.settings['MYSQL_PASSWD']
        self.db = self.settings['MYSQL_DBNAME']
        # 连接数据库
        self.connect = pymysql.connect(host=self.host, db=self.db, user=self.user, passwd=self.passwd, charset='utf8',
                                       use_unicode=False)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        try:
            sql, params = item.distinct_data()
            self.cursor.execute(sql, params)
            data = self.cursor.fetchone()
            if data:
                pass
            else:
                # 插入数据
                sql, params = item.get_insert_sql()
                self.cursor.execute(sql, params)
                self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            print(error)
        return item
