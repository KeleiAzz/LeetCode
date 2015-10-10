__author__ = 'keleigong'
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 5
        res = 0
        while i <= n:
            res += n / i
            i *= 5
        return res

s = Solution()
a = 1808548329
print s.trailingZeroes(a)