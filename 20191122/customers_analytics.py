#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 12/2/2019 8:23 PM
#@Author: lee
#@File  : customers_analytics.py
# csv主要是,为主的数据隔开

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from  matplotlib.pyplot import MultipleLocator
from  pandas import Series

# 直接读取CSV格式数据,未清洗数据  shape[0]行数 shape[1]列数
customers = pd.read_csv("E:\\Python\\20191122\\customers_export_1.csv")
customers_column = customers.shape[0]
customers_row    = customers.shape[1]
customers_spent  = customers['Total Spent'].sum()
print('处理数据前总客户数量：%d人，共%d列的客户维度数据,一共消费了%.2f美刀' % (customers_column,customers_row,customers_spent))
# print(customers.info()) #查看索引、数据类型、内存大小

# 根据total spent 的0得到的人数区分出购买了的和没购买的 分出只有邮箱的 没支付的也有接受调查的和没调查的
customers_dis_pay    = customers[ customers["Total Spent"]==0].shape[0]
customers_only_email = customers[(customers["Total Spent"]==0)&(customers['Country'].isnull())].shape[0]
customers_cancel_pay = customers[(customers["Total Spent"]==0)&(customers['Country'].notnull())].shape[0]
customers_cancel_pay_yes = customers[(customers["Total Spent"]==0)&(customers['Country'].notnull())&(customers['Accepts Marketing'] == 'yes')].shape[0]
customers_cancel_pay_no  = customers[(customers["Total Spent"]==0)&(customers['Country'].notnull())&(customers['Accepts Marketing'] == 'no')].shape[0]

print('处理数据中未消费客户：%d人，只填邮箱的客户：%d人,填了地址的客户：%d人' % (customers_dis_pay,customers_only_email,customers_cancel_pay))
print('处理数据中未消费总户：填了地址接受营销的客户：%d人,不接受营销的客户：%d人'% (customers_cancel_pay_yes,customers_cancel_pay_no))
# 根剧total spent 不为0的人
customers_spent_pay     =  customers[customers["Total Spent"]!=0].shape[0]
customers_spent_pay_yes =  customers[(customers["Total Spent"]!=0) &(customers['Accepts Marketing'] == 'yes')].shape[0]
customers_spent_pay_no  =  customers[(customers["Total Spent"]!=0) &(customers['Accepts Marketing'] == 'no')].shape[0]
print('处理数据中消费的客户：%d人，接受营销的客户：%d人,不接受营销的客户：%d人'% (customers_spent_pay,customers_spent_pay_yes,customers_spent_pay_no))

# 调节图形大小，宽，高
plt.figure(figsize=(12,10))
# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
#定义饼状图的标签，标签是列表
labels = ['未消费只填邮箱','未消费填了地址接受营销','未消费填了地址不接受营销','消费了接受营销','消费了不接受营销']
#每个标签占多大，会自动去算百分比
sizes  = [customers_only_email,customers_cancel_pay_yes,customers_cancel_pay_no,customers_spent_pay_yes,customers_spent_pay_no]
colors = ['coral','pink','hotpink','cornflowerblue','lightskyblue']
#将某部分爆炸出来， 使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
explode = (0.05,0.05,0.05,0.07,0.01)
#labeldistance， 文本的位置离远点有多远，1.1指1.1倍半径的位置
#autopct，       圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
#shadow，        饼是否有阴影
#startangle，    起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
#pctdistance，   百分比的text离圆心的距离

#patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本
patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 0,pctdistance = 0.6)
# 改变文本的大小 方法是把每一个text遍历。调用set_size方法设置它的属性
for t in l_text:
    t.set_size=(30)
for t in p_text:
    t.set_size=(20)
# 设置x，y轴刻度一致，这样饼图才能是圆的
plt.axis('equal')
plt.legend()
# plt.show()

# 删除所有列First Name 为空值的行（清理完数据）
customers =  customers[customers["Total Spent"]!=0]
print('处理数据后消费的客户：%d人，未消费的客户：%d人' % (customers.shape[0],customers_column-customers.shape[0]))

# 根据国家code 某地区总消费数和订单总数
# 根据省级code 某地区消费总数和订单总数
# 根据消费的钱来划分端集中在什么段的人群消费多
country_code_spent = customers.groupby(['Country Code','Total Orders']).sum()
country_code_spent.plot(kind='bar') #种类使用块 bar条型 line折线
plt.xlabel('订单日期(日)',color='k',fontsize=20)
plt.ylabel('每日购买金额(元)',color='k',fontsize=20)
province_code_spent = customers.groupby(['Province Code','Total Orders']).sum()
province_code_spent.plot(kind='bar') #种类使用块 bar条型 line折线

spent_moeny = customers['Total Spent']
plt.rcParams['figure.figsize'] = (14, 5)    #设定图片大小
f = plt.figure()                            #确定画布
f.add_subplot(1,2,1)
sns.distplot(spent_moeny, kde=False)        #绘制频数直方图
plt.ylabel("消费钱人数统计", fontsize=16)
plt.ylim((0,2500))
plt.xlim((0,500))
plt.xticks(fontsize=16)                  #设置x轴刻度值的字体大小
plt.yticks(fontsize=16)                  #设置y轴刻度值的字体大小
plt.title("(a)", fontsize=20)            #设置子图标题
plt.show()
f.add_subplot(1,2,2)
sns.distplot(spent_moeny)                #绘制密度直方图
plt.ylabel("密度", fontsize=16)
plt.xticks(fontsize=16)                  #设置x轴刻度值的字体大小
plt.yticks(fontsize=16)                  #设置y轴刻度值的字体大小
plt.title("(b)", fontsize=20)            #设置子图标题
plt.subplots_adjust(wspace=0.3)          #调整两幅子图的间距
plt.show()








