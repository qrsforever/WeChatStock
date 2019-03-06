#!/usr/bin/python3
# -*- coding: utf-8 -*-

__all__ = ['MessageQueue']

#  from multiprocessing import Queue
from queue import Queue
from threading import Condition

class MessageQueue(object):

    """Docstring for MessageQueue. """

    def __init__(self):
        self.cond = Condition()
        self.queue = Queue()

    def enqueue_message(self, msg):
        self.cond.acquire()
        self.queue.put(msg)
        self.cond.notify()
        self.cond.release()

    def remove_message(self, msg):
        print("Not support")

    def next(self):
        self.cond.acquire()
        if self.queue.empty():
            self.cond.wait()
        msg = self.queue.get()
        self.queue.task_done()
        self.cond.release()
        return msg

