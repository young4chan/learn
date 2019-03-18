#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager

# send task to queue
task_queue = queue.Queue()
# receive result from queue
result_queue = queue.Queue()

# inherit from BaseManager to QueueManager
class QueueManager(BaseManager):
    pass

# register two queues to network, associate callable para to Queue objects:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# bind port 5000, set checksum 'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# start Queue:
manager.start()
# acquire Queue object through network
task = manager.get_task_queue()
result = manager.get_result_queue()
# put several tasks in
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# get result from queue
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# close:
print('master exit.')

