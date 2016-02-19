# -*- coding: utf-8 -*-
from collections import deque

__author__ = 'gaochenchao'


class PushAndPop(object):

    def __init__(self):
        self.stack = deque([])

    def verify(self, pushsequence=None, popsequence=None):
        i = 0
        for j in popsequence:
            if self.stack and self.stack[-1] == j:
                self.stack.pop()
            else:
                while True:
                    if i >= len(pushsequence):
                        return False

                    if j != pushsequence[i]:
                        self.stack.append(pushsequence[i])
                        i += 1
                    else:
                        i += 1
                        break
        return True


pap = PushAndPop()
print pap.verify([1, 2, 3, 4, 5], [4, 5, 3, 1, 2])
