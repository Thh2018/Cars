# encoding = utf-8
# @Software: PyCharm
# @Environment: Python3.6.1


from scrapy import cmdline

# cmdline.execute("scrapy crawl article_list".split()) # 爬取文章列表
# cmdline.execute("scrapy crawl article_content".split()) # 爬取文章内容
# cmdline.execute("scrapy crawl article_comment".split())  # 爬取文章评论内容
# cmdline.execute("scrapy crawl article_serices".split())  # 爬取文章车系
cmdline.execute(("scrapy crawl article_pv").split())  # 爬取文章阅读数
