#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

# create local ThreadLocal object:
local_school = threading.local()

def process_student():
    # acquire student associated with the current thread
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # bind student with ThreadLocal
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
