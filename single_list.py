# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class ListNode(object):

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        return "[ListNode] %s" % self.value


class LnTool(object):

    def __init__(self):
        self.head = ListNode(None, None)

    def arrToList(self, arr):
        if not arr or len(arr) == 0:
            return self.head
        p = self.head
        for i in arr:
            ln = ListNode(i, None)
            p.next = ln
            p = p.next
        return self.head

    def printList(self):
        p = self.head
        while p:
            if p.value:
                print p.value
            p = p.next

    def getLen(self):
        p = self.head
        if not p.next:
            return 0
        count = 0
        while p:
            count += 1
            p = p.next
        return count - 1

    def getBackN(self, n):
        p = self.head
        if not p.next:
            return self.head
        ln_len = self.getLen()
        m = ln_len - n
        if n > ln_len:
            m = ln_len
        for i in range(0, m+1):
            p = p.next
        return p

    def getBackN2(self, n):
        p0 = self.head
        p1 = self.head
        i = 1
        while i <= n:
            p1 = p1.next
            i += 1
        while p1:
            p0 = p0.next
            p1 = p1.next
        return p0

    def delBackN(self, n):
        p0 = self.head
        p1 = self.head
        if not p0.next:
            return
        for i in range(n+1):
            p1 = p1.next
        while p1:
            p0 = p0.next
            p1 = p1.next
        p0.next = p0.next.next

    def removeNode(self, val):
        if not self.head.next:
            return self.head
        newHead = ListNode(None, self.head)
        pre = newHead
        p = self.head
        while p:
            if p.value == val:
                pre.next = p.next
                p = p.next
            else:
                pre = p
                p = p.next
        return newHead.next

    def removeDuplicate(self):
        pre = self.head
        p = self.head.next
        while p:
            if pre.value == p.value:
                while p and pre.value == p.value:
                    p = p.next
                pre.next = p
            else:
                pre = p
                p = p.next

    def removeAllDuplicate(self):
        if not self.head or not self.head.next:
            return self.head
        newHead = ListNode(None, self.head)
        pre = newHead
        p = self.head
        next = None
        while p and p.next:
            next = p.next
            if p.value == next.value:
                while p and next and p.value == next.value:
                    next = next.next
                pre.next = next
                p = next
            else:
                pre = p
                p = p.next

    def reverseBetween(self, m, n):
        newHead = ListNode(None, self.head)
        if m == n:
            return
        k = 0
        front = newHead
        while k < m:
            front = front.next
            k += 1
        pre = front.next
        p = pre.next
        next = None
        tail = pre
        while k < n:
            next = p.next
            p.next = pre
            pre = p
            p = next
            k += 1
        tail.next = p
        front.next = pre
        self.head = newHead.next


lnt = LnTool()
# arr = [1, 2, 3, 4, 5, 6]
# lnt.arrToList(arr)
# arr = [1, 2, 6, 4, 5, 6, 2]
arr = [1, 2, 3, 4, 5, 6, 7]
lnt.arrToList(arr)
# lnt.printList()
# lnt.removeAllDuplicate()
lnt.printList()
lnt.reverseBetween(3, 6)
lnt.printList()