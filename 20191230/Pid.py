#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 12/31/2019 9:08 AM
#@Author: lee
#@File  : Pid.py

import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import os

time_length = 600
time_sample = 100
time_interval = float(time_length/time_sample)
error_coeff = 3
t = np.linspace(0,time_length,time_sample)
Slope = 1
Intercept = 0
standard_in = 20

# The system model
system_model = lambda i : Slope*i + Intercept
standard_out = system_model(standard_in)
print("The Standard Output:%d" % standard_out)

Kp = 0.08 # average
Ki = -0.7 # intergre
Kd = 0.01 # diff

error_bef = []
real_out_ajust = []
real_out_ajust.append(70)
real_out_ajust.append(75)
error_bef.append(real_out_ajust[0]-standard_out)
Out_plt = np.linspace(standard_out,standard_out,time_sample)

# 标准直接计算公式1：Pout=Kp*e(t) + Ki*Sum[e(t)] + Kd*[e(t) - e(t-1)]
def PID_Controller_Direct_Mem(standard_out,t):
        global time_sample,Kp,Ki,Kd,error_bef,real_out_ajust
        if t > time_sample:
                print("Time Out! Quit!")
                return -1
        error_now = real_out_ajust[t] - standard_out
        error_bef.append(error_now) # 记录了所有的误差
        integrate_res = np.sum(error_bef)
        Diffirent_res = error_now - error_bef[t-1]
        return Kp*error_now + Ki*integrate_res + Kd*Diffirent_res

for t_slice in range(1,time_sample-1):
        Pout = PID_Controller_Direct_Mem(standard_out,t_slice)
        real_out_ajust.append(system_model(Pout))

plt.figure('PID_Controller_Direct_Mem')
plt.xlim(0,time_length)
plt.ylim(0,2*standard_out)
plt.plot(t,real_out_ajust)
plt.plot(t,Out_plt)
plt.show()