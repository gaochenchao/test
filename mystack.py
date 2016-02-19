# -*- coding: utf-8 -*-
from MyQueue import MyQueue

__author__ = 'gaochenchao'


class MyStack(object):

    def __init__(self):
        self.size = 0
        self.stack = []

    def push(self, arg):
        self.stack.append(arg)
        self.size += 1

    def pop(self):
        if not self.isEmpty():
            val = self.stack.pop()
            self.size -= 1
            return val
        else:
            return None

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def Len(self):
        return self.size

    def peek(self):
        if not self.isEmpty():
            return self.stack[self.size - 1]
        return None

    def Print(self):
        print self.stack


class TwoQueStack(object):

    def __init__(self):
        self.size = 0
        self.queue1 = MyQueue()
        self.queue2 = MyQueue()

    def empty(self):
        if self.size == 0:
            return True
        return False

    def push(self, arg):
        if self.queue1.isEmpty() and self.queue2.isEmpty():
            target = self.queue1
        else:
            target = self.queue1 if not self.queue1.isEmpty() else self.queue2ssss
        target.offer(arg)
        self.size += 1

    def pop(self):
        if self.empty():
            return
        if self.queue1.isEmpty():
            i = self.size
            while i > 1:
                self.queue1.offer(self.queue2.pull())
                i -= 1
            self.queue2.pull()
            self.size -= 1
        else:
            i = self.size
            while i > 1:
                self.queue2.offer(self.queue1.pull())
                i -= 1
            self.queue1.pull()
            self.size -= 1

    def top(self):
        if self.empty():
            return
        if self.queue1.isEmpty():
            i = self.size
            while i > 1:
                self.queue1.offer(self.queue2.pull())
                i -= 1
            print self.queue2.peek()
            self.queue1.offer(self.queue2.pull())
        else:
            i = self.size
            while i > 1:
                self.queue2.offer(self.queue1.pull())
                i -= 1
            print self.queue1.peek()
            self.queue2.offer(self.queue1.pull())


if __name__ == "__main__":
    ts = TwoQueStack()
    ts.push(1)
    ts.push(2)
    ts.push(3)
    ts.push(4)
    ts.push(5)
    ts.push(6)
    ts.pop()
    ts.pop()
    ts.pop()
    ts.top()
    ts.top()
