class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        i2 = i3 = i5 = -1
        x = v2 = v3 = v5 = 1
        for k in range(n):
            x = min(v2, v3, v5)
            dp[k] = x
            if x == v2:
                i2 += 1
                v2 = dp[i2] * 2
            if x == v3:
                i3 += 1
                v3 = dp[i3] * 3
            if x == v5:
                i5 += 1
                v5 = dp[i5] * 5
        return dp[-1]
        