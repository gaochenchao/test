from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True
            
        sdict = defaultdict(list)
        tdict = defaultdict(list)
        for i in s:
            sdict[i].append(0)
        for j in t:
            tdict[j].append(0)
        print sdict
        print tdict
        if sdict == tdict:
            return True
        else:
            return False

cls = Solution()
print cls.isAnagram("world hello", "hello world")