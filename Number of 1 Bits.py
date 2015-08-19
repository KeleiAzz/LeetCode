__author__ = 'keleigong'
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        a = bin(n)[2:]
        x = 0
        for i in a:
            if i == '1':
                x += 1
        return x


s = Solution()

print(s.hammingWeight(2))