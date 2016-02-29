# TODO Need to improve efficiency, solve with DP


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        size = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    n = 0
                    while True:
                        if self.is_square(matrix, i, j, n):
                            size = max(size, n + 1)
                            n += 1
                        else:
                            break

        return size ** 2

    def is_square(self, matrix, i, j, n):
        if n == 0:
            return True
        if i + n == len(matrix) or j + n == len(matrix[0]):
            return False
        for k in range(j, j + n + 1):
            if matrix[i + n][k] == "0":
                return False
        # if any([x == "0" for x in matrix[i+n][j:j+n+1]]):
        #     return False
        for k in range(i, i + n + 1):
            if matrix[k][j + n] == "0":
                return False
                # if any([x[j+n] == "0" for x in matrix[i:i+n+1]]):
                # return False
        return True

    def squareDP(self, matrix):
        if not matrix or not matrix[0]: return 0
        nrow, ncol, dp = len(matrix), len(matrix[0]), [[1 if c == '1' else 0 for c in row] for row in matrix]
        for i in range(nrow):
            for j in range(ncol):
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        print dp

s = Solution()

grid = ["1101", "1101", "1111"]

print s.maximalSquare(grid)

s.squareDP(grid)