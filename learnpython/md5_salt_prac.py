#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, passowrd):
        self._username = username
        self._salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self._password = get_md5(passowrd + self._salt)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

def login(username, password):
    user = db[username]
    return user._password == get_md5(password + user._salt)

if __name__ == '__main__':
    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('ok')

