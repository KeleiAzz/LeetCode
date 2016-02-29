__author__ = 'keleigong'
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n == 1 or m == 1:
            return 1
        if n == 0 or m == 0:
            return 0
        matrix = []
        for i in range(m-1):
            matrix.append([0] * n)
            matrix[i][-1] = 1
        matrix.append([1] * n)
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]
        return matrix[0][0]