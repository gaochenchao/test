# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


def muti(n):
    if n == 1:
        print 'f(%s)压栈，到达最大深度' % str(n)
        print 'f(%s)出栈' % str(n)
        return 1
    print 'f(%s)压栈' % str(n)
    result = n * muti(n-1)
    n *= 10
    print n
    print "f(%s)出栈" % str(n)
    return result

print muti(5)
