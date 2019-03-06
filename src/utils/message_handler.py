#!/usr/bin/python3
# -*- coding: utf-8 -*-

__all__ = ['MessageHandler']

from message import Message

class MessageHandler(object):

    """Docstring for MessageHandler. """

    def __init__(self, queue):
        self.message_queue = queue

    def send_message(self, what, **args):
        print(type(args), args)
        msg = Message.obtain(self, what, args)
        self.message_queue.enqueue_message(msg)

    def send_message_delay(self, when, what, **args):
        print("not support yes!")
