cache = {}
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s in cache:
            return cache[s]
        for i in range(len(s)-1):
            if s[i:i+2] == '++':
                if not self.canWin(s[:i]+'--'+s[i+2:]):
                    cache[s[:i]+'--'+s[i+2:]] = False
                    cache[s] = True
                    return True
        return False