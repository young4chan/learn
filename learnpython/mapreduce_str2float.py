#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

def fn(x, y):
    return 10 * x + y

def gn(x, y):
    return y + x * 0.1

def char2num(c):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[c]

def str2float(s):
    s1, s2 = s.split('.')
    return reduce(fn, map(char2num, s1)) + 0.1 * reduce(gn, map(char2num, s2[::-1]))

print(str2float('123.456'))
print(str2float('123456789.13579'))

    
