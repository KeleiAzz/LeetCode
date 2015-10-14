__author__ = 'keleigong'
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = list(s)
        b = list(t)
        d = {}
        for i in range(len(a)):
            if a[i] in d.keys():
                if d[a[i]] == b[i]:
                    pass
                else:
                    return False
            else:
                d[a[i]] = b[i]
        d ={}
        for i in range(len(a)):
            if b[i] in d.keys():
                if d[b[i]] == a[i]:
                    pass
                else:
                    return False
            else:
                d[b[i]] = a[i]
        return True

so = Solution()

s = 'aba'
t = 'bab'
print so.isIsomorphic(s, t)