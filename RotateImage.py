__author__ = 'keleigong'
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        for i in range(n + 1):
            for j in range(i, n - i, 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i] = matrix[n-i][n-j]
                matrix[n-i][n-j] = matrix[j][n-i]
                matrix[j][n-i] = tmp
        for line in matrix:
            print line

s = Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])
