# -*- coding: utf-8 -*-
from collections import deque

__author__ = 'gaochenchao'


class Solution(object):

    def valid(self, arg):
        if not arg or len(arg) == 0:
            return True
        if len(arg) % 2 != 0:
            return False
        stack = []
        for i in arg:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if i == ")":
                    if stack.pop() != "(":
                        stack = []
                        return False

                if i == "]":
                    if stack.pop() != "[":
                        stack = []
                        return False

                if i == "}":
                    if stack.pop() != "{":
                        stack = []
                        return False
        if len(stack) == 0:
            return True
        else:
            stack = []
            return False

so = Solution()
print so.valid("{([]})")
print so.valid("{([])}()[[")
print so.valid("{()}[]")
# print so.valid("")