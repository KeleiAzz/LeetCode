class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        pre, cur = 1, 1
        for i in range(1, len(s)):
            if s[i] == '0':
                cur = 0
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                pre, cur = cur, cur + pre
            else:
                pre = cur
        return cur

s = Solution()

a = "1245236749"

print s.numDecodings(a)