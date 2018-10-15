# coding = utf-8
# @Software: PyCharm
# @Environment: Python3.6.1
import scrapy
from scrapy.spiders import CrawlSpider
from models import article
from item import article_content_items
from tools.ExtractArticle import extract_article


class AutoHomeArticleContentSpider(CrawlSpider):
    name = "article_content"
    article_id_list = article.StructureArticleID().get_article_id()
    article_id_index = 0
    base_url = "https://cont.app.autohome.com.cn/cont_v8.5.0/content/news/newscontent-pm2-n%s-t0-rct1-ish0-ver%s.json"
    start_urls = [base_url % (
        article_id_list[article_id_index][0],
        article_id_list[article_id_index][1])]

    def parse(self, response):
        yield scrapy.Request(url=response.url,
                             callback=self.parse_article_content_items,
                             dont_filter=True)

    def parse_article_content_items(self, response):
        item = article_content_items.ArticleContentScrapyItem()
        item['id'] = self.article_id_list[self.article_id_index][0]
        item['content'] = extract_article(response.url)
        yield item
        self.article_id_index += 1
        if self.article_id_index < len(self.article_id_list):
            url = self.base_url % (
            self.article_id_list[self.article_id_index][0],
            self.article_id_list[self.article_id_index][1])
            yield scrapy.Request(url=url,
                                 callback=self.parse_article_content_items,
                                 dont_filter=True)
