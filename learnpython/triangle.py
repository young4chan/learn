#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def triangle(n):
    L = [1]
    while n > 0:
        yield L
        L = [L[x] + L[x+1] for x in range(len(L) - 1)]
        L.insert(0, 1)
        L.append(1)
        n = n -1
    return 'done'

        
