class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if n == 0 or m == 0 or not positions:
            return []
        find = {}
        count = 0
        res = []
        for i, j in positions:
            idx = self.getIndex(i, j, m, n)
            if idx not in find:
                count += 1
                find[idx] = idx
                up, right, down, left = self.getIndex(i+1, j, m, n), self.getIndex(i, j+1, m, n), \
                self.getIndex(i-1, j, m, n),self.getIndex(i, j-1, m, n)
                for neighbor in [up, right, down, left]:
                    if neighbor >= 0 and neighbor in find:
                        fneighbor = self.getAnc(find, neighbor)
                        fidx = self.getAnc(find, idx)
                        if fneighbor != fidx:
                            count -= 1
                            find[fidx] = fneighbor
                            find[idx] = fneighbor
                res.append(count)
            else:
                pass
        return res


    def getAnc(self, find, position):
        father = find[position]
        while father != find[father]:
            father = find[father]
        return father


    def getIndex(self, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n:
            return -1
        return i * n + j