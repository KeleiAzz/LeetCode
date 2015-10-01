__author__ = 'keleigong'
class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        a = [1, 1, 2, 5]
        if n > 3:
            for i in range(4,n+1,1):
                a.append(0)
                for j in range(1,i+1):
                    a[i] += a[j-1]*a[i-j]
        return a[n]
