# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Environment: Python3.6.1
import scrapy


class ArticleSeriesItems(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    ver = scrapy.Field()
    page_id = scrapy.Field()
    series_id = scrapy.Field()
    series_name = scrapy.Field()
    pv_count = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """INSERT INTO auto_home_article_series (article_id,series_id) VALUES (%s, %s) """
        params = (self['id'], self['series_id'])
        return insert_sql, params

    def distinct_data(self):
        query = """select id from auto_home_article_series where article_id =%s and series_id = %s"""
        params = (self["id"], self["series_id"])
        return query, params

