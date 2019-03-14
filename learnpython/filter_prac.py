#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def _is_palindrome(n):
    return str(n) == str(n)[::-1]

output = filter(_is_palindrome, range(1, 1000))
print('1~1000:', list(output))
    
