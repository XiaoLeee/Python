#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 12/27/2019 1:34 PM
#@Author: lee
#@File  : UrlFiter.py

from bs4 import BeautifulSoup
import pandas as pd
import re
import time
from datetime import datetime
import matplotlib.pyplot  as plt
import matplotlib.dates as mdates
import jieba
import wordcloud
import imageio
import base64
# 打开文件 获得html句柄内容
HtmlUrl = 'C:\\Users\\Nero\\Desktop\\M_Code\\Python\\20191227\\bookmarks_12_27_19.html'
htmlfile = open(HtmlUrl,'r',encoding='utf-8')
htmlhandle = htmlfile.read()

# 创建数据集准备excel的表格输出
result = pd.DataFrame({},index=[0]) #dataframe就是多列的数据集 series是一列
result['link'] = ''
result['title'] = ''
result['time'] = ''
result['icon'] = ''
new = result

# 数据集特征得到href链接 标题 时间戳 icon图标
soup = BeautifulSoup(htmlhandle,'lxml')
for link in soup.find_all('a'):
    new['link'] = link.get('href')   # 获取到的链接信息
    new['title'] = link.string       # 链接内容文本信息即标题
    time_local = time.localtime(int(link['add_date']))      # 获取得到的时间戳注意用小写 str转换为int整型
    new['time'] = time.strftime("%Y-%m-%d %H:%M:%S",time_local)  # 转换为年月日 小时分钟秒
    new['icon'] = link.get('icon')   # 获取得到的ICON图标值 暂时不处理图片
    result = result.append(new,ignore_index=True)

# 想法1 根据时间排序得到不同时间段的信息 可以分析长期喜欢看什么内容
result = result.drop_duplicates('link',keep='first')  # 去重获得重复的值 false是重复的都去掉
result.sort_values('time',inplace=True)               # keywords使用time或link进行排序
print(result['link'][0])

# 得到表格数据开始对数据集进行处理 (注意是否是字符串的问题比较,其实是去重后需要新保存)
# 想法2 根据相同网站链接数进行排序得信息 可以分析哪个网站访问的实际多 利用词云进行统计
# result = result.drop_duplicates('link',keep='first')  # 去重获得重复的值 false是重复的都去掉
# result.sort_values('link',inplace=True)               # keywords使用time或link进行排序
# keyWords = result[result['title'].notnull()]['title'] # 剔除标题title为空的数据值

# 获取Series列的数据行拼接再直接 进行分词拼接为字符串
# seg_list ='\n'.join(str(row) for index,row in keyWords.items())
# seg_list = jieba.cut(seg_list, cut_all=False)
# seg_str = " ".join(seg_list)
# 将字符串处理输入到txt文本
# with open("wordsRs.txt", "w",encoding='utf-8') as f:
#     f.write(seg_list)

# 进行词云处理
# mk = imageio.imread("cat.png")
# w = wordcloud.WordCloud(mask=mk)
# w = wordcloud.WordCloud(width=1920,height=1080,background_color='white',font_path="爱度综艺简体.ttf",mask=mk,scale=15) # 参数配置 长 宽 背景
# w.generate(seg_str)              # 传入文本
# w.to_file('output-urlwords.png') # 输出图片拟合

# 想法3 获取得到的图标处理后批量同意生成.PNG的格式
# result = result.drop_duplicates('icon',keep='first')  # 去重获得重复的值 false是重复的都去掉
# result.sort_values('time',inplace=True)               # keywords使用 time 或link进行排序
# result = result[result['icon'].notnull()]             # 剔除掉icon为空的数据值
# count = 0
# for key,val in result['icon'].items():
#      val = val.replace('data:image/png;base64,', '').replace('%0A', '\\n')
#      imgdata = base64.b64decode(val)
#      file = open( "icon/"+str(count)+'.png', 'wb')
#      count+= 1
#      file.write(imgdata)
#      file.close()

# 保存Csv格式问题
# result.to_csv('C:\\Users\\Nero\\Desktop\\M_Code\\Python\\20191227\\link.csv')