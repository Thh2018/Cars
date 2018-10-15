#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-19 15:55:54
# @Author  : hunk (qiang.liu@ikooo.cn)
# @Version : Python 3.5.0
import time
import datetime

"""
UTC 时间格式 = "2014-09-18T10:42:16.126Z"
GMT 时间格式 = "Thu, 07 Dec 2017 04:01:57 GMT"
"""


def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def get_current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_time(stringTime):
    """字符串时间格式化timestamp类型"""
    return datetime.datetime.strptime(stringTime, '%Y-%m-%d')


def get_current_gmt_date():
    """获取格林尼治标准时"""
    date = datetime.datetime.strftime(datetime.datetime.utcnow(), "%a, %d %b %Y %H:%M:%S GMT")
    return date


def get_yesterday_date():
    """获取昨天的日期"""
    today = datetime.date.today()
    offset = datetime.timedelta(days=1)
    yesterday = today - offset
    return yesterday


def utc_to_local(utcStruct):
    """UTC时间转本地时间（+8: 00）"""
    nowStamp = time.time()  # 返回当前时间的时间戳
    localTime = datetime.datetime.fromtimestamp(nowStamp)  # 时间戳转换成字符串日期时间
    utcTime = datetime.datetime.utcfromtimestamp(nowStamp)  # 时间戳转换成UTC日期时间
    zoneOffset = localTime - utcTime
    localStruct = utcStruct + zoneOffset
    return localStruct


def local_to_utc(localStruct):
    """本地时间转UTC时间（-8: 00）"""
    timeStruct = time.mktime(localStruct.timetuple())
    return datetime.datetime.utcfromtimestamp(timeStruct)


def timestamp_to_localtime(timeStamp):
    # 转换成localtime
    time_local = time.localtime(timeStamp//1000)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    return time.strftime("%Y-%m-%d", time_local)


if __name__ == '__main__':
    # print(get_current_gmt_date())
    print(get_current_date())
    # utc = "2014-09-18T10:42:16.126Z"
    # UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"  # UTC时间格式
    # LOCAL_FORMAT = "%Y-%m-%d %H:%M:%S"  # 本地时间格式
    # utc_st = datetime.datetime.strptime(utc, UTC_FORMAT)
    # print(utc_st)
    # print(utc_to_local(utc_st))
    # print(get_yesterday_date())
