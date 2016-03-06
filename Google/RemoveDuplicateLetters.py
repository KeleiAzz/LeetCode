class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        res = s[0]
        lastAppear = {v : i for i, v in enumerate(s)}
        for i in range(1, len(s)):
            if s[i] not in res:
                while res and s[i] < res[-1] and lastAppear[res[-1]] > i:
                    res = res[:-1]
                res += s[i]
        return res
