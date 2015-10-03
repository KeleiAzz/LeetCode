__author__ = 'keleigong'
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1]]
        for i in range(2, numRows+1, 1):
            tmp = []
            tmp.append(1)
            for j in range(len(res[-1]) -1):
                tmp.append(res[-1][j] + res[-1][j+1])
            tmp.append(1)
            res.append(tmp)
        return res


