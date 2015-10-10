__author__ = 'keleigong'
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n = n >> 1
        return ans
