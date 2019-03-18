#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def name_of_email(addr):
    rege = re.match(r'^<?([0-9a-zA-Z\.\_\s]*)>?\s*?([0-9a-z\.\_]*)@(\w*?).(\w*)$', addr)
    print(rege.groups())
    if rege:
        return rege.group(1)
    else:
        return False

if __name__ == '__main__':
#    assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
#    assert name_of_email('tom@voyager.org') == 'tom'
    print(name_of_email('<Tom Paris> tom@voyager.org'))
    print(name_of_email('young.chan@live.com'))
    print('ok')
