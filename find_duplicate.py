# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class Solution(object):

    def findDuplicated(self, arr):
        n = len(arr)
        fast = n - 1
        slow = n - 1
        while True:
            slow = arr[slow] - 1
            fast = arr[fast] - 1
            fast = arr[fast] - 1
            if slow == fast:
                break
        slow = n - 1
        while slow != fast:
            slow = arr[slow] - 1
            fast = arr[fast] - 1
        return slow + 1

sou = Solution()
arr = [2, 7, 1, 3, 5, 3, 4, 6]
print sou.findDuplicated(arr)