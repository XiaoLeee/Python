#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 4/27/2020 8:16 PM
#@Author: lee
#@File  : psql.py

import  pymysql

# open sql
db = pymysql.connect("119.23.246.50","plan","Tn2e5keYckYT3zyf","plan");
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print(data)
# close sql
db.close()
