#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

def pi(N):
    # step 1
    ns = itertools.count(start=1, step=2)
    # step 2
    ns = itertools.takewhile(lambda x: x <= 2*N-1, ns)
    # step 3
    L = []
    for i in ns:
        L.append((-1)**((i+1)/2%2+1)*4/i)
    # step 4
    return sum(L)

if __name__ == '__main__':
    print(pi(10))
    print(pi(100))
    print(pi(1000))
    print(pi(10000))
    assert 3.04 < pi(10) < 3.05
    assert 3.13 < pi(100) < 3.14
    assert 3.140 < pi(1000) < 3.141
    assert 3.1414 < pi(10000) < 3.1415
    print('ok')
