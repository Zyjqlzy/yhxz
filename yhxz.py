#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yhxz_base
import logger

log = logger.Log()
classify_list = yhxz_base.get_classify_list()  # 分类list：['/', '/qingchun/', '/xinggan/', '/siwa/', '/hanguo/', '/riben/', '/xiezhen/', '/a/jingpindongtai/', '/a/chengrenmanhua/', '/a/guochanzipai/', '/a/ziyuanxiazai/']
for classify in classify_list[1:7]:
    request_url = yhxz_base.base_url + classify
    parse = yhxz_base.send_requests(request_url)
    page_list = parse.xpath('//div[@class="page"]/ul/li/select[@name="sldd"]/option/@value').extract()
    for i in range(len(page_list)):
        album_url = request_url + page_list[i]
        album_parse = yhxz_base.send_requests(album_url)
        album_list = album_parse.xpath('//div[@class="list"]/ul/li/a/@href').extract()
        print(album_list)
        for x in range(len(album_list)):
            photo_url = yhxz_base.base_url + album_list[x]
            photo_parse = yhxz_base.send_requests(photo_url)
            photo_page_list = photo_parse.xpath('//div[@class="page"]/ul/li/a/@href').extract()
            photo = photo_parse.xpath('//div[@id="disappear"]/a/img/@src').extract()
            print(photo)
            for y in range(2, len(photo_page_list)):
                photo_next_url = request_url + '/' + photo_page_list[y]
                photo_next_parse = yhxz_base.send_requests(photo_next_url)
                photo = photo + photo_next_parse.xpath('//div[@id="disappear"]/a/img/@src').extract()
                print(photo)
# href_list = parse.xpath('//div[@class="list"]/ul/li/a/@href').extract()
# page_list = parse.xpath('//div[@class="page"]/ul/li/select[@name="sldd"]/option/@value').extract()
# print(page_list)
# for page in page_list:
#     url = base_url + page
#     print(url)


# for href in href_list:
#     new_url = base_web + href
#     href_data = requests.get(new_url).text
