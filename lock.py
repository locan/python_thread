# -*- coding:utf-8 -*-
'''锁
'''
import time
from threading import Thread, Lock

value = 0
lock = Lock()


def get_lock():
    global value
    new = value + 1
    time.sleep(0.001)
    value = new


def get_has_lock():
    global value
    with lock:
        new = value + 1
        time.sleep(0.001)
        value = new

threads = []

for i in range(100):
    #t = Thread(target=get_has_lock)
    t = Thread(target=get_lock)
    t.start()
    threads.append(t)

for t in threads:
    t.join()


print value