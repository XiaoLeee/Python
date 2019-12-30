#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 11/22/2019 11:00 PM
#@Author: lee
#@File  : music.py

import librosa
import librosa.display
import matplotlib.pyplot as plt

# Get the music path
filepath = 'E:\\Python\\20191122\\'
filename = filepath+'music.wav'
print(filename)

# Load the music to lib
x,sr =librosa.load(filename,sr=8000)
print(x.shape,sr)

# show the music
plt.figure(figsize=(14, 5))
librosa.display.waveplot(x,sr=sr)
# plt.savefig('figpath.svg')
plt.show()

# X   = librosa.stft(x)
# Xdb = librosa.amplitude_to_db(abs(X))   # 把幅度转成分贝格式
# plt.figure(figsize=(14, 5))
# librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
# plt.colorbar()
# plt.title("TO the DB")
# plt.savefig('figpath.svg')
# plt.show()

