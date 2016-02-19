# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class ListNode(object):

    def __init__(self, v, next):
        self.v = v
        self.next = next

    def __repr__(self):
        return "[ListNode] %s" % self.v


class Joephus(object):

    def __init__(self):
        self.head = ListNode(None, None)

    def arrToCircle(self, arr):
        p = self.head
        for i in arr:
            p.next = ListNode(i, None)
            p = p.next
        p.next = self.head.next
        return self.head.next

    def printLi(self, head):
        if not head:
            return
        p = head
        while p:
            print p
            p = p.next

    def getStart(self, head, start):
        if start <= 0:
            return head
        p = head
        for i in range(1, start):
            p = p.next
        return p

    def countAndRemove(self, startNode, step):
        pre = startNode
        for i in range(1, step - 1):
            pre = pre.next
        print pre.next
        pre.next = pre.next.next
        return pre.next

    def joephous(self, head, n, start, step):
        startNode = self.getStart(head, start)
        for i in range(0, n):
            startNode = self.countAndRemove(startNode, step)
        startNode.next = None


class Intersection(object):

    def __init__(self):
        self.head = ListNode(None, None)

    def printLi(self, head):
        if not head:
            return
        p = head
        while p:
            print p
            p = p.next

    def arrToInter(self, arr1, arr2, intersect):
        head1 = ListNode(None, None)
        head2 = ListNode(None, None)
        join = None
        p1 = head1
        p2 = head2
        for i in arr1:
            p1.next = ListNode(i, None)
            p1 = p1.next
            if i == intersect:
                join = p1
        for i in arr2:
            p2.next = ListNode(i, None)
            p2 = p2.next
        p2.next = join
        return head1.next, head2.next

    def arrToCircle(self, arr,  index=None):
        p = self.head
        join = None
        for i in range(0, len(arr)):
            p.next = ListNode(arr[i], None)
            if index and i == index-1:
                join = p
            p = p.next
        if join:
            p.next = join.next
        return self.head.next

    def getLen(self, head):
        p = head
        count = 0
        while p:
            count += 1
            p = p.next
        return count

    def findJoin(self, head1, head2):
        m = self.getLen(head1)
        n = self.getLen(head2)
        p1 = head1
        p2 = head2
        if not m or not n:
            return
        if m > n:
            for i in range(0, m - n):
                p1 = p1.next
        if m < n:
            for i in range(0, n - m):
                p2 = p2.next
        while p1 and p2:
            if p1 == p2:
                return p2
            else:
                p1 = p1.next
                p2 = p2.next
        return None

    def hasCircle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print slow
                return True
        return False

    def getJoin(self, head):
        if not head:
            return None
        slow = head
        fast = head
        hascircle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hascircle = True
                break

        if not hascircle:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast





its = Intersection()
arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
h = its.arrToCircle(arr1, 4)
print its.getJoin(h)
# its.printLi(h)
# print its.findJoin(h1, h2)