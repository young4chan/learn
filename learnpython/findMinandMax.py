#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def findMinandMax(L):
    if len(L) == 0:
        return (None, None)
    min = L[0]
    max = L[0]
    for i in L:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min, max)
