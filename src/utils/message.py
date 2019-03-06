#!/usr/bin/python3
# -*- coding: utf-8 -*-

__all__ = ['Message']

class Message(object):

    """Docstring for Message. """

    def __init__(self, handler, what):
        self.handler = handler
        self.what = what
        self.when = 0
        self.args = None

    @staticmethod
    def obtain(handler, what, args):
        msg = Message(handler, what)
        if args:
            msg.args = args
        print(type(args), msg.args)
        return msg

    def __str__(self):
        return "handler:{} what:{} args:{}".format(self.handler, self.what, self.args)
