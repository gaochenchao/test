# -*- coding: utf-8 -*-


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __cmp__(self, other):
        if self.age > other.age:
            return 1
        elif self.age < other.age:
            return -1
        else:
            return 0

    def __repr__(self):
        return "[person] %s age: %s" %(self.name, self.age)


class ListNode(object):

    def __init__(self, v, next):
        self.v = v
        self.next = next

    def __repr__(self):
        return "[v] %s [next] %s" % (self.v, self.next.v)


class MiniLink(object):
    # head = ListNode(None, None)

    def __init__(self):
        self.head = ListNode(None, None)

    def printList(self):
        p = self.head.next
        while p.next:
            print p
            p = p.next
        print "=============================="

    def listToLink(self, arr):
        p = self.head
        for i in arr:
            node = ListNode(i, None)
            p.next = node
            p = node

    def insert(self, index, v):
        p = self.head
        i = 0
        while i <= index:
            p = p.next
            i += 1
        node = ListNode(v, None)
        node.next = p.next
        p.next = node

    def remove(self, index):
        p = self.head
        i = 0
        while i < index:
            p = p.next
            i += 1
        nx = p.next
        if nx:
            p.next = nx.next
        else:
            p.next = None

    def recurse(self, node):
        if node.next:
            self.recurse(node.next)
            print node
        else:
            print "[v] %s [next] None" % node.v

    def reversePrint(self):
        self.recurse(self.head)

    def getMax(self):
        p = self.head.next
        max = p
        while p.next:
            p = p.next
            max = max if p.v <= max.v else p
        return max.v

if __name__ == '__main__':
    link = MiniLink()
    # arr = [1, 2, 3, 4, 5]
    # link.listToLink(arr)
    # link.reversePrint()
    # link.insert(2, 9)
    # link.printList()
    # link.remove(0)
    # link.printList()
    p1 = Person('a', 29)
    p2 = Person('b', 30)
    p3 = Person('bc', 181)
    p4 = Person('bd', 34)
    p5 = Person('bg', 30)
    # arr = [p1, p2, p3, p4, p5]
    arr = [1, 2, 3, 4, 5]
    link.listToLink(arr)
    link.reverseLink()
    link.printList()
    # print link.getMax()
