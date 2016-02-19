# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class LinkNode(object):

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __repr__(self):
        return "[LinkNode] value=%s" % self.value


class ReverseLinkedList(object):

    def __init__(self):
        pass

    def arrayToLink(self, arr):
        head = LinkNode(None, None)
        p = head
        for i in arr:
            node = LinkNode(i, None)
            p.next = node
            p = node
        return head

    def printLink(self, head):
        p = head.next
        while p:
            if p.value:
                print p
            p = p.next

    def reverseLink(self, head):
        pre = head
        p = head.next
        next = None
        while p:
            next = p.next
            p.next = pre
            pre = p
            p = next
        head.next = None
        return LinkNode(None, pre)

    def recurse(self, p):
        if not p.next:
            return p
        else:
            next = p.next
            node = self.recurse(next)
            next.next = p
            return node

    def recursizeReverse(self, head):
        if not head or not head.next:
            return head
        node = self.recurse(head)
        head.next = None
        # print node
        return LinkNode(None, node)



arr = [1, 2, 3, 4, 5, 6]
link = ReverseLinkedList()
head = link.arrayToLink(arr)
# link.printLink(head)
# head = link.reverseLink(head)
head = link.recursizeReverse(head)
link.printLink(head)


