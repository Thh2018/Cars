# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 10:30
# @Author  : Hunk
# @Email   : qiang.liu@ikooo.cn
# @File    : ExtractArticle.py
# @Software: PyCharm


from newspaper import Article


def extract_article(article_url):
    try:
        article = Article(article_url, language='zh')
        article.download()  # 文章下载
        article.parse()  # 解析文章
        return article.text  # 返回文章内容
    except Exception as e:
        return ""


if __name__ == "__main__":
    url = 'https://cont.app.autohome.com.cn/cont_v8.5.0/content/news/newscontent-pm2-n914511-t0-rct1-ish0-ver20180320182000.json'
    print(extract_article(url))
