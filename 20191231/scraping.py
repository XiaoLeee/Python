#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 12/30/2019 6:27 PM
#@Author: lee
#@File  : scraping.py

import builtwith
import whois
result = builtwith.parse('https://www.loopeve.com') #获取得到网站使用技术
whoisname = whois.whois('loopeve.com')
print(whoisname)