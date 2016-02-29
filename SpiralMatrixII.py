__author__ = 'keleigong'
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # matrix = [[0] * n] * n
        matrix = []
        for i in range(n):
            matrix.append([0] * n)
        top = right = bottom = n
        left = n
        x = 1
        while x <= n ** 2:
            for i in range(4):
                if i == 0:
                    for j in range(n-top, top, 1):
                        matrix[n-top][j] = x
                        x += 1
                    top -= 1

                elif i == 1:
                    for j in range(n-right+1, right, 1):
                        matrix[j][right-1] = x
                        x += 1
                    right -= 1
                elif i == 2:
                    for j in range(bottom-2, n-bottom-1, -1):
                        matrix[bottom-1][j] = x
                        x += 1
                    bottom -= 1
                elif i == 3:
                    for j in range(left-2, n-left, -1):
                        matrix[j][n-left] = x
                        x += 1
                    left -= 1
        return matrix

s = Solution()

s.generateMatrix(4)


import re
def check_js(text):
    res = re.findall(r'\"(.+?)\"', text)
    print res

# text