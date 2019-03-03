#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def trim(s):
    if s == '':
        return s

    while s[0] == ' ':
        s = s[1:]
        if s == '':
            return s
    while s[-1] == ' ':
        s = s[:-1]
        if s == '':
            return s
    return s
