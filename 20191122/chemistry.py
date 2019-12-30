#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 12/3/2019 12:09 PM
#@Author: lee
#@File  : chemistry.py


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 读取两列实验数据
experiment = pd.read_csv("E:\\Python\\20191122\\experiment.csv",header=None)
experiment_cols1 = experiment.iloc[:,0]
# print(experiment_cols1)
experiment_cols1.plot(kind='line',rot=30)
plt.show()

