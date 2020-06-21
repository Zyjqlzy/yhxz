#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logger
import requests
import parsel

base_url = 'http://yhxz521.com'
log = logger.Log()


def get_classify_list():
    log.debug("***********开始爬取***********")
    pase = send_requests(base_url)
    href_list = pase.xpath('//div[@class="nav"]/ul/li/a/@href').extract()  # 分类list
    log.debug("分类list为：%s" % href_list)
    return href_list


def send_requests(url):
    response = requests.get(url)
    log.debug("请求地址：%s" % url)
    response.encoding = response.apparent_encoding
    log.debug("编码为：%s" % response.encoding)
    html = response.text  # response的html
    parse = parsel.Selector(html)
    return parse


if __name__ == "__main__":
    get_classify_list()
