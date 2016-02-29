# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Pint[]} operators an array of point
    # @return {int[]} an integer array
    def numIslands2(self, n, m, operators):
        # Write your code here
        cells = [-1] * (n * m)
        find = {}
        # for i in range(n*m):
            # find[i] = i
        count = 0
        res = []
        for operator in operators:
            i, j = operator.x, operator.y
            index = self.getIndex(i, j, n, m)
            if index >= 0 and index not in find:
                find[index] = index
                count += 1
                surround = [self.getIndex(i+1, j,n,m), self.getIndex(i,j+1,n,m), \
                self.getIndex(i-1,j,n,m), self.getIndex(i,j-1,n,m)]
                for idx in surround:
                    if idx >=0 and idx in find:
                        findex = self.findAnc(find, index)
                        fidx = self.findAnc(find, idx)
                        if findex != fidx:
                            count -= 1
                            find[findex] = fidx
                            find[index] = fidx
            res.append(count)
        return res



    def findAnc(self, find, i):
        father = find[i]
        while father != find[father]:
            father = find[father]
        return father


    def getIndex(self, i, j, n, m):
        if i < 0 or j < 0 or i >= n or j >= m:
            return -1
        return i * m + j
