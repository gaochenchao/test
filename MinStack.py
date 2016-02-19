# -*- coding: utf-8 -*-
from collections import deque

__author__ = 'gaochenchao'


class MinStack(object):

    def __init__(self):
        self.stack = deque([])
        self.minstack = deque([])

    def push(self, arg):
        if len(self.stack) == 0:
            self.stack.append(arg)
            self.minstack.append(arg)
        else:
            self.stack.append(arg)
            k = arg if arg < self.minstack[-1] else self.minstack[-1]
            self.minstack.append(k)

    def pop(self):
        if len(self.stack) == 0:
            return
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        print self.stack[-1]

    def getMin(self):
        print self.minstack[-1]

ms = MinStack()
for i in [9, 4, 5, 7, 3, 6, 8]:
    ms.push(i)
ms.top()
ms.getMin()
ms.pop()
ms.getMin()
ms.push(2)
ms.getMin()