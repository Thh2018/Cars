# coding = utf-8
# @Software: PyCharm
# @Environment: Python3.6.1
import pymysql
from scrapy.utils.project import get_project_settings


class DBHelper(object):
    def __init__(self):
        self.settings = get_project_settings()
        self.host = self.settings['MYSQL_HOST']
        self.port = self.settings['MYSQL_PORT']
        self.user = self.settings['MYSQL_USER']
        self.passwd = self.settings['MYSQL_PASSWD']
        self.db = self.settings['MYSQL_DBNAME']

    # 连接MySQL
    def connect_mysql(self):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                               passwd=self.passwd, charset='utf8')
        return conn

    # 连接指定数据库
    def connect_database(self):
        conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                               passwd=self.passwd, db=self.db, charset='utf8')
        return conn

    # 创建数据库
    def create_database(self):
        conn = self.connect_mysql()

        sql = "create database if not EXISTS " + self.db
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.close()

    # 数据库插入操作
    def insert(self, sql, *params):
        conn = self.connect_database()

        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        cursor.close()
        conn.close()

    # 数据库查询操作
    def query(self, sql, *params):
        conn = self.connect_database()

        cursor = conn.cursor()
        cursor.execute(sql, params)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    # 数据库更新操作
    def update(self, sql, *params):
        conn = self.connect_database()

        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        cursor.close()
        conn.close()

    # 数据库删除操作
    def delete(self, sql, *params):
        conn = self.connect_database()

        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        cursor.close()
        conn.close()
