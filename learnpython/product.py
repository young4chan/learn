#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def product(*args):
    s = 1
    for arg in args:
        s = s * arg
    return s

