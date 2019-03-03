#!/usr/bin/env python3
# -*- coding: utf-8 -*-

h = input('Please input height: ')
w = input('Please input weight: ')
height = float(h)
weight = float(w)

bmi = weight / (height ** 2)

print(bmi)

if bmi < 18.5:
    print('You are too light')
elif (bmi >= 18.5) & (bmi < 25):
    print('You are in normal state')
elif (bmi >= 25) & (bmi < 28):
    print('You are overweight')
elif (bmi >= 28) & (bmi < 32):
    print('You are fat')
else:
    print('You are too fat')
