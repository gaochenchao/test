# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class ListNode(object):

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        return "[ListNode] %s" % self.value


class ListManual(object):

    def __init__(self):
        self.head = ListNode(None, None)

    def arrToLi(self, arr):
        p = self.head
        for i in arr:
            p.next = ListNode(i, None)
            p = p.next
        return self.head

    def printLi(self, head=None):
        head = head if head else self.head
        p = head
        while p:
            if p.value:
                print p
            p = p.next

    def lenL(self):
        if not self.head.next:
            return 0
        n = 0
        p = self.head.next
        while p:
            n += 1
            p = p.next
        return n

    def rotateRight(self, k):
        n = self.lenL()
        if k == 0:
            return
        if k > n:
            k = n % k
        if k == 0:
            return
        newTail = self.head
        i = 0
        while i < n - k:
            newTail = newTail.next
            i += 1
        newHead = newTail.next
        join = newTail
        while join.next:
            join = join.next
        newTail.next = None
        join.next = self.head.next
        self.head = newHead

    def isParlindrom(self):
        n = self.lenL()
        central = int(n/2)
        rstart = self.head
        i = 0
        while i < central:
            rstart = rstart.next
            i += 1
        if n % 2 != 0:
            rstart = rstart.next
        join = rstart
        pre = rstart.next
        tail = pre
        p = pre.next
        while p.next:
            next = p.next
            p.next = pre
            pre = p
            p = next
        p.next = pre
        join.next = p
        tail.next = None
        lstart = self.head.next
        rstart = join.next
        j = 1
        while j <= central:
            if lstart.value != rstart.value:
                return False
            lstart = lstart.next
            rstart = rstart.next
            j += 1
        return True

    def swapPaire(self):
        begin = self.head
        pre = begin.next
        p = pre.next
        while pre and p:
            next = p.next
            p.next = pre
            pre.next = next
            begin.next = p
            if not next:
                break
            else:
                begin = pre
                pre = next
                p = pre.next

    def partion(self, x=3):
        if not self.head.next:
            return
        leftLn = ListNode(None, None)
        rightLn = ListNode(None, None)
        leftTail = leftLn
        rightTail = rightLn
        p = self.head.next
        while p:
            if p.value < x:
                leftTail.next = p
                leftTail = p
            else:
                rightTail.next = p
                rightTail = p
            p = p.next
        rightTail.next = None
        leftTail.next = rightLn.next
        self.head = leftLn

    def reverse(self, begin):
        if not begin or not begin.next:
            return
        newHead = ListNode(None, begin)
        pre = newHead
        p = pre.next
        while p.next:
            next = p.next
            p.next = pre
            pre = p
            p = next
        p.next = pre
        begin.next = None
        newHead.next = p
        return newHead.next

    def reorderLn(self):
        leftStart = self.head.next
        leftEnd = leftStart
        n = self.lenL()
        k = int(n/2)
        if n % 2 != 0:
            k += 1
        for i in range(1, k):
            leftEnd = leftEnd.next
        rightStart = leftEnd.next
        rightStart = self.reverse(rightStart)
        flag = True
        while rightStart.next:
            if flag:
                next = leftStart.next
                leftStart.next = rightStart
                leftStart = next
            else:
                next = rightStart.next
                rightStart.next = leftStart
                rightStart = next
            flag = not flag
            print rightStart, leftStart

lm = ListManual()
arr = [1, 2, 3, 4, 5, 6]
# arr = [1, 4, 3, 2, 5, 2]

head = lm.arrToLi(arr)
h = lm.reorderLn()
# lm.partion(3)
# h = lm.reverse(head)
# lm.printLi(h)
# lm.swapPaire()
# lm.rotateRight(3)
# lm.printLi()
# print lm.isParlindrom()