# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class Solution(object):

    def indexOf(self, heack, needle):
        if len(needle) == 0:
            return True
        for i in range(0, len(heack)):
            count = 0
            m = i
            for j in range(0, len(needle)):
                if heack[m] == needle[j]:
                    count += 1
                    m += 1
                    if count == len(needle):
                        return i
                else:
                    break
        return -1

    def indexOf02(self, heack, needle):
        x = len(heack)
        y = len(needle)
        for i in range(0, x):
            count = 0
            for j in range(0, y):
                if i + j > x:
                    break
                if heack[i+j] != needle[j]:
                    break
                else:
                    count += 1
            if count == y:
                return i
        return -1
print Solution().indexOf("helloworld", "ow")
print Solution().indexOf02("helloworld", "ow")