#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    if(a == 0):
        raise TypeError('wrong variable')
    else:
        delta = math.sqrt(b*b - 4*a*c)
        return (-b + delta)/(2*a), (-b - delta)/(2*a)
