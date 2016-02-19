# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ""
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        result = "11"
        for i in range(3, n+1):
            temp = ""
            count = 1
            cmp = result[0]
            for j in range(1, len(result)):
                if result[j] == cmp:
                    count += 1
                else:
                    temp += "%s%s" % (str(count), cmp)
                    count = 1
                    cmp = result[j]
            temp += "%s%s" % (str(count), cmp)
            result = temp
        return result


print Solution().countAndSay(5)
print Solution().countAndSay(6)
print Solution().countAndSay(7)
