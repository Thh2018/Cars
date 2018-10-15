# -*- coding: utf-8 -*-
import scrapy


class AutohomeSpider(scrapy.Spider):
    name = 'autohome'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['http://autohome.com.cn/']

    def parse(self, response):
        pass
