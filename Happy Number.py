__author__ = 'keleigong'
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        k = 0
        while k < 10:
            l = list(str(n))
            n = sum([int(i) ** 2 for i in l])
            if n == 1:
                return True
            k += 1
        return False