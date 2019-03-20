#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

def safe_base64_decode(s):
    return base64.b64decode(s) if len(s) % 4 == 0 else safe_base64_decode(s + b'=')

if __name__ == '__main__':
    assert b'abcd' == safe_base64_decode(b'YWJjZA'), print(safe_base64_decode('YWJjZA'))
    assert b'abcd' == safe_base64_decode(b'YWJjZA=='), print(safe_base64_decode('YWJjZA=='))
