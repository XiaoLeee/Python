#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 11/23/2019 5:17 PM
#@Author: lee
#@File  : customers.py

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas import Series

# 直接读取数据,未清洗数据
customers = pd.read_excel("E:\\Python\\20191122\\demo.csv")

# 处理包含空白行数据前后 列数 df.shape[1] 行数 shape[0]
before_customers_tol = customers.shape[0]
customers.dropna(axis=0, how='any', inplace=True)
after_customers_tol  = customers.shape[0]

# 客户地区重复数的一列
# repeat_customers_tol = dict(customers['Province'].value_counts())
# 这个公式dict提取出来的数据需要重新写入到一个数组列 但并不一定需要dict
hist_province_count = customers['Province'].value_counts()
print(hist_province_count[:10])
hist_province_count.plot(kind='bar',rot=30,xticks= 10)
plt.show()

# 方法1.1： 绘画直方图观察消费数据
# fig = plt.figure()
# ax1 = fig.add_subplot(3,3,1)
# ax1.hist(customers['Total Spent'],bins=10)
# plt.title('Customer Spend Moeny')
# plt.xlabel('Money')
# plt.ylabel('#Customers')
# plt.show()

# 方法1.2: 直方图统计客户消费
# sns.distplot(customers['Total Spent'])
# # print(before_customers_tol)
# # print(after_customers_tol)
# plt.xlim((0,100))
# plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
# plt.show()

# 方法二： 绘制线箱图
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.boxplot(customers['Total Spent'])
# plt.show()

# 方法三： 小提琴图
# sns.violinplot(customers['Country Code'],customers['Total Spent'])
# sns.despine()
# plt.show()

# 方法4： 条形图
# var = customers.groupby('Country Code').sum()
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
# ax1.set_xlabel('Country Code')
# ax1.set_ylabel('Sum of Spent Money')
# ax1.set_title('Loaction sum of Spent Money')
# var.plot(kind='bar') #种类使用块
# plt.show()

# 方法5: 地区客户折线图
# var = customers.groupby('Country Code').sum()
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
# ax1.set_xlabel('Country Code')
# ax1.set_ylabel('Sum of Spent Money')
# ax1.set_title('Loaction sum of Spent Money')
# var.plot(kind='line') #种类使用折线
# plt.show()

# 方法6：堆叠柱状图
# var = customers.groupby(['Country Code','Province']).sum()
# var.unstack().plot(kind='bar',stacked=True,color=['red','blue'],grid = True)
# plt.show()
# plt.savefig('fig.png', bbox_inches='tight') #保存导出图像

# 方法7：散点图
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.scatter(customers['Country Code'],customers['Total Spent'])
# plt.show()

# 方法8：泡泡图
# fig = plt.figure()
# ax  = fig.add_subplot(1,1,1)
# ax.sacatter(customers['Country Code'],customers['Total Spent'],s=customers['tef'])
# plt.show()

# 方法9：饼状图
# var = customers.groupby(['Country Code']).sum().stack()
# temp = var.unstack()
# type(temp)
# x_list = temp['Sales']
# label_list = temp.index
# pyplot.axis("equal") #The pie chart is oval by default. To make it a circle use pyplot.axis("equal")
# #To show the percentage of each pie slice, pass an output format to the autopctparameter
# plt.pie(x_list,labels=label_list,autopct="%1.1f%%")
# plt.title("Pastafarianism expenses")
# plt.show()