class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        uppercase = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
        res = ''
        while True:
            res = uppercase[n%26] + res
            if n <= 26:
                break
            n = (n - 1) / 26
        return res