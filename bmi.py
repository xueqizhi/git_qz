#! /usr/bin/env python3
# -*- coding: utf-8 -*-
height = input('your height: (m)')
weight = input('your weight: (kg)')
h = float(height)
w = float(weight)
bmi = w / (h *h)
print('your bmi is %.1f' % bmi)
print('and you are :')
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('过于肥胖')
