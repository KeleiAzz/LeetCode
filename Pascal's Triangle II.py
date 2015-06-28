__author__ = 'keleigong'

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        pt = [[1,1]]
        for i in range(2, rowIndex + 1):
            tmp =[1]
            for j in range(0, len(pt[-1])-1):
                tmp.append(pt[-1][j]+pt[-1][j+1])
            tmp.append(1)
            pt.append(tmp)
        print pt
        return pt[-1]


s = Solution()

print s.getRow(3)