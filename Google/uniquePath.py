class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        dp = [ [1] + [0] * (n-1) for _ in range(m)]
        dp[0] = [1] * n
        print dp
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print dp
        return dp[-1][-1]
        # return math.factorial(m+n-2) / (math.factorial(m-1) * math.factorial(n-1))

s = Solution()

s.uniquePaths(2,2)