#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools

def createCounter():
    f = [0]
    def counter():
        f[0] = f[0] + 1
        return f[0]
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
counterB = createCounter()
print([counterB(), counterB(), counterB(), counterB()])
