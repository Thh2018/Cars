# coding = utf-8
# @Software: PyCharm
# @Environment: Python3.6.1
import json

import math
import scrapy
from scrapy.spider import CrawlSpider

from item.article_comment_items import ArticleCommentScrapyItem
from models.article import StructureArticleID
from tools.GetCurrentTime import get_current_date


class AutoHomeArticleCommentSpider(CrawlSpider):
    name = "article_comment"
    article_list = StructureArticleID().get_article_id()
    article_index = 0
    page_index = 0
    last_time = 0
    base_url = "https://newsnc.app.autohome.com.cn/reply_v7.9.0/news/comments-pm2-n%s-o0-s20-lastid%s-t0.json"
    start_urls = [base_url % (article_list[article_index][0], last_time)]

    def parse(self, response):
        yield scrapy.Request(url=response.url,
                             callback=self.parse_article_comment_items,
                             dont_filter=True)

    def parse_article_comment_items(self, response):
        item = ArticleCommentScrapyItem()
        content = json.loads(response.body.decode(), strict=False)
        comment_list = content["result"]["list"]
        for comment in comment_list:
            item["article_id"] = self.article_list[self.article_index][0]
            item["comment_id"] = comment["id"]
            item["floor"] = comment["floor"]
            item["user_id"] = comment["nameid"]
            item["publish_time"] = comment["time"]
            item["content"] = comment["content"]
            item["update_time"] = get_current_date()
            yield item
        self.last_time = item["comment_id"]
        self.page_index += 1
        # 向上取整（总评论数/每页评论20条）> 页数
        if math.ceil(content["result"]["totalcount"] / 20) >= self.page_index:
            url = self.base_url % (
                self.article_list[self.article_index][0], self.last_time)
            yield scrapy.Request(url=url,
                                 callback=self.parse_article_comment_items,
                                 dont_filter=True)
        else:
            self.article_index += 1
            if self.article_index < len(self.article_list):
                self.page_index = 1
                self.last_time = 0
                url = self.base_url % (
                self.article_list[self.article_index][0], self.last_time)
                print(url)
                yield scrapy.Request(url=url,
                                     callback=self.parse_article_comment_items,
                                     dont_filter=True)
