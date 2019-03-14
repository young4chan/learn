#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, 1000 * (end - start)))
        return fn(*args, **kw)
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

print(fast(1, 2))

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y *z

print(slow(1, 2, 3))


