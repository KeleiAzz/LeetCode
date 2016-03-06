class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        def dfs(matrix, i, j, prev):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] <= prev:
                return -1
            if dp[i][j] > 0:
                return dp[i][j]
            cur = matrix[i][j]
            up = dfs(matrix, i + 1, j, cur)
            right = dfs(matrix, i, j + 1, cur)
            down = dfs(matrix, i - 1, j, cur)
            left = dfs(matrix, i, j - 1, cur)

            steps = max(up, right, down, left, 0)
            dp[i][j] = max(dp[i][j], 1 + steps)
            return 1 + steps
        max_steps = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_steps = max(max_steps, dfs(matrix, i, j, -float('INF')))
        print dp
        return max_steps


input = [[9,9,4],[6,6,8],[2,1,1]]
s =Solution()
print s.longestIncreasingPath(input)