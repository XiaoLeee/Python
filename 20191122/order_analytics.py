#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 12/8/2019 5:56 PM
#@Author: lee
#@File  : order_analytics.py


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import Series
from mpl_toolkits.mplot3d import Axes3D

# 直接读取CSV格式数据,未清洗数据  shape[0]行数 shape[1]列数
orders = pd.read_csv("E:\\Python\\20191122\\orders_export_1.csv")
orders_column = orders.shape[0]
orders_row    = orders.shape[1]
customers_spent  = orders['Total'].sum()
print('处理数据前总订单数量：%d单，共%d列的订单维度数据,一共消费了%.2f美刀' % (orders_column,orders_row,customers_spent))
# print(customers.info()) #查看索引、数据类型、内存大小

order_spent = orders.groupby(['Name','Total']).sum()
print(order_spent)

# 创建画布 将3维转换为3维
fig = plt.figure()
order_3d = fig.add_subplot(1, 1, 1, projection='3d')
# X, Y value 的值
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)
order_3d.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
plt.show()