from math import sqrt
# cache = {}
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        dp = [float('INF')] * (n+1)
        for i in range(1, n+1):
            sqt = int(sqrt(i))
            if sqt * sqt == i:
                dp[i] = 1
            else:
                dp[i] = 1 + min([dp[i-j*j] for j in range(1, sqt+1)])
        return dp[-1]
