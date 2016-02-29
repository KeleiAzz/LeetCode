class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x

        absn = abs(n)
        half = self.myPow(x, absn/2)
        if absn % 2 == 0:
            res = half * half
        else:
            res = half * half * x

        if n > 0:
            return res
        else:
            return 1 / res
