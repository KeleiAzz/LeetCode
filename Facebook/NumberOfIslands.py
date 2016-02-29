class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        grid = map(list, grid)
        res = []
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.expand(grid, i, j)
                    # map(lambda x: grid[x[0]][x[1]] = "#", lands)
                    # for land in lands:
                    #     grid[land[0]][land[1]] = "#"
                    # res.extend(lands)
        return count


    def expand(self, grid, i, j):
        if (0 <= i < len(grid)) and (0 <= j < len(grid[0])) and grid[i][j] == '1':
            grid[i][j] = "#"
            self.expand(grid, i, j+1)
            self.expand(grid, i+1, j)
            self.expand(grid, i, j-1)
            self.expand(grid, i-1, j)
        else:
            return

        # return res

s = Solution()

grid = ["111", "111", "111"]

print s.numIslands(grid)