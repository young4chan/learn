#!/usr/bin/env python3
# -*- coding: utf-

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()    # initial sequence
    while True:
        n = next(it)    # return first element from sequence
        yield n
        it = filter(_not_divisible(n), it)  # create a new sequence


for n in primes():
    if n < 1000:
        print(n)
    else:
        break
