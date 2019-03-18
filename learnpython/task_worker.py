#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, sys, queue
from multiprocessing.managers import BaseManager

# create QueueManager:
class QueueManager(BaseManager):
    pass

# register queue with name, as QueueManager acquire Queue from network
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# connect server
server_addr = '192.168.1.2'
print('Connect to server %s...' % server_addr)
# set port and checksum
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# connect
m.connect()
# acquire Queue object
task = m.get_task_queue()
result = m.get_result_queue()
# get tasks from task queue, write result to result queue
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# processing end
print('worker exit.')

