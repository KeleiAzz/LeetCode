class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0:
            return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        nrow = len(obstacleGrid)
        ncol = len(obstacleGrid[0])
        dp = [[0] * ncol for _ in range(nrow)]
        # dp[0][0] = 1
        for i in range(nrow):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        print dp
        for i in range(ncol):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break
        print dp
        for i in range(1, nrow):
            for j in range(1, ncol):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print dp
        return dp[-1][-1]


s = Solution()
m = [[0,0],[1,0]]
print s.uniquePathsWithObstacles(m)