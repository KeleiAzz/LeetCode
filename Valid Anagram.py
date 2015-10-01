__author__ = 'keleigong'
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            try:
                t.remove(s[i])
                s.remove(s[i])
            except:
                return False
        return True

s = Solution()

print s.isAnagram('a', 'a')