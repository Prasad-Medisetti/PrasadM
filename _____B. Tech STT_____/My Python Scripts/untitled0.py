# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 10:29:40 2019

@author: hp
"""

from datetime import datetime
n = int(input())
l = []
for i in range(n):
    pro, date = input().split(',')
    l.append((pro,date))
dt = [int(i) for i in input().split('-')]
dt = datetime(dt[2],dt[1],dt[0])
print(l)
s = []
for i in l:
    dt1 = [int(i) for i in i[1].split('-')]
    if dt1>dt:
        s.append(i)
