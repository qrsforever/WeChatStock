#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time, os
#  from multiprocessing import Queue, Process
from message_queue import MessageQueue
from message_handler import MessageHandler

from threading import Thread

handler1 = None
handler2 = None

class OneMessageHandler(MessageHandler):
    def __init__(self, queue):
        MessageHandler.__init__(self, queue)

    def handle_message(self, msg):
        print("Another handle_message")
        pass

class AnotherMessageHandler(MessageHandler):
    def __init__(self, queue):
        MessageHandler.__init__(self, queue)

    def handle_message(self, msg):
        print("Another handle_message")
        pass

def dispatch_message(queue):
    while True:
        msg = queue.next()
        print(msg)

def send_message_process():
    print("process:{}".format(os.getpid()))
    handler1.send_message(1, a='a', b='b')
    time.sleep(3)
    handler2.send_message(2, c='c', d='d')

def unit_test_utils():
    queue = MessageQueue()
    handler1 = OneMessageHandler(queue)
    handler2 = AnotherMessageHandler(queue)
    #  process = Process(target=dispatch_message, args=(queue,))
    #  process = Process(target=send_message_process, args=(handler,))
    process = Thread(target=send_message_process)
    process.start()
    print("process:{}".format(os.getpid()))
    dispatch_message(queue)


if __name__ == "__main__":
    unit_test_utils()
