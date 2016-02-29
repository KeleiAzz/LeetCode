__author__ = 'keleigong'
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 1:
            return sum(grid[0])
        if len(grid[0]) == 1:
            return sum([row[0] for row in grid])
        for i in range(len(grid) - 2, -1, -1):
            grid[i][-1] += grid[i+1][-1]
        for j in range(len(grid[0]) - 2, -1, -1):
            grid[-1][j] += grid[-1][j+1]
        for i in grid:
            print i
        print
        for i in range(len(grid) - 2, -1, -1):
            for j in range(len(grid[0]) - 2, -1, -1):
                grid[i][j] += min(grid[i+1][j], grid[i][j+1])
                print i, j
        for i in grid:
            print i
        return grid[0][0]


s = Solution()
grid = [[1,2,5],[3,2,1]]
print s.minPathSum(grid)