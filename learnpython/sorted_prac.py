#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def by_name(t):
    return t[0]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(L, key=by_name))

def by_score(t):
    return 1/t[-1]

print(sorted(L, key=by_score))
