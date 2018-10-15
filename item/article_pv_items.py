# coding = utf-8
# @Software: PyCharm
# @Environment: Python3.6.1
import scrapy


class ArticlePVScrapyItem(scrapy.Item):
    article_id = scrapy.Field()
    pv_count = scrapy.Field()
    update_time = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = """insert into auto_home_article_pv (article_id,pv_count,update_time) VALUES (%s, %s, str_to_date(%s,'%%Y-%%m-%%d'))"""
        params = (self["article_id"], self["pv_count"], self["update_time"])
        return insert_sql, params

    def distinct_data(self):
        query = """select id from auto_home_article_pv where id =%s"""
        params = (0)
        return query, params
