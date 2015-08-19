__author__ = 'keleigong'
class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        if num==0:
            return 0
        return num%9 if num%9!=0 else 9

s = Solution()

a = 9912

print s.addDigits(a)