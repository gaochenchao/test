# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class UglyNumber(object):

    def verify(self, num):
        if num <= 0:
            return False
        if num == 1:
            return True

        while num % 2 == 0:
            num /= 2

        while num % 3 == 0:
            num /= 3

        while num % 5 == 0:
            num /= 5

        print num
        if num == 1:
            return True
        return False

    def bigUgly(self, arg=1352):
        if arg < 1:
            return
        if arg == 1:
            return 1
        count = 1
        m = 1
        m2 = [m*2]
        m3 = [m*3]
        m5 = [m*5]
        while count < arg:
            # print m2, m3, m5
            m = min(m2[0], m3[0], m5[0])
            m2.append(m*2)
            m3.append(m*3)
            m5.append(m*5)
            if m2[0] == m:
                m2.pop(0)
            if m3[0] == m:
                m3.pop(0)
            if m5[0] == m:
                m5.pop(0)
            count += 1
        return m


ugn = UglyNumber()
print ugn.bigUgly()
# print ugn.verify(180)