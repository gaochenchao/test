# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class SimplifyPath(object):

    def simplify(self, arg):
        stack = []
        if arg == "" or not arg:
            return
        if arg == "/":
            return "/"
        arr = arg.split("/")
        for i in arr:
            if not i or i == ".":
                continue
            else:
                if i == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
        if not stack:
            return "/"
        return "/" + "/".join(stack)

sp = SimplifyPath()
print sp.simplify("/../../")
print sp.simplify("/home//foo/")
print sp.simplify("a/./b/../../../c/d/")