#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def is_valid_email(addr):
    if re.match(r'^([0-9a-zA-Z\.\_]*)@(\w*?)(.com)$', addr):
        print(re.match(r'^([0-9a-zA-Z\.\_]*)@(\w*?)(.com)$', addr).groups())
        return True
    return False

if __name__ == '__main__':
    assert is_valid_email('someone@gmail.com')
    assert is_valid_email('bill.gates@microsoft.com')
#    assert is_valid_email('bob#example.com')
    assert is_valid_email('mr-bob@example.com')
    print('ok')
    
