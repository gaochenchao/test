# -*- coding: utf-8 -*-
# from mystack import MyStack

__author__ = 'gaochenchao'


class QueNode(object):

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


class MyQueue(object):

    def __init__(self):
        self.head = QueNode(None, None)
        self.last = self.head
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def Len(self):
        return self.size

    def offer(self, arg):
        node = QueNode(arg, None)
        self.last.next = node
        self.last = node
        self.size += 1

    def pull(self):
        if self.isEmpty():
            return None
        node = self.head.next
        after = node.next
        self.head.next = after
        self.size -= 1
        if self.size == 0:
            self.last = self.head
        return node.value

    def peek(self):
        return self.head.next.value


# mq = MyQueue()
# mq.offer(1)
# mq.offer(2)
# mq.offer(3)
# mq.pull()
# mq.pull()
# print mq.peek()
#
# class MyQueue2(object):
#
#     def __init__(self):
#         self.stack1 = MyStack()
#         self.stack2 = MyStack()
#         self.size = 0
#
#     def isEmpty(self):
#         if self.size == 0:
#             return True
#         return False
#
#     def Len(self):
#         return self.size
#
#     def offer(self, arg):
#         self.stack1.push(arg)
#         self.size += 1
#
#     def pull(self):
#         if self.size == 0:
#             return
#
#         if self.stack2.isEmpty():
#             while not self.stack1.isEmpty():
#                 self.stack2.push(self.stack1.pop())
#         self.stack2.pop()
#         self.size -= 1
#
#     def peek(self):
#         if self.size == 0:
#             return
#
#         if self.stack2.isEmpty():
#             while not self.stack1.isEmpty():
#                 self.stack2.push(self.stack1.pop())
#         # print self.stack2.Len()
#         print self.stack2.peek()
#
# que = MyQueue2()
# for i in range(88, 99):
#     que.offer(i)
#
# # que.peek()
# # que.pull()
# # que.peek()
#
# for i in range(0, que.Len()):
#     que.peek()
#     que.pull()


