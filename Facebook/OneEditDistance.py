class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False
        i = 0
        while i < len(s) and i < len(t) and s[i] == t[i]:
            i += 1

        if s[i+1:] == t[i:] or s[i:] == t[i+1:] or s[i+1:] == t[i+1:]:
            return True
        return False