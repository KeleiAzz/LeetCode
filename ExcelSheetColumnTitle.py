__author__ = 'keleigong'
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        letters = 'ZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ''
        while n > 0:
            reminder = n % 26
            res = letters[reminder] + res
            # if reminder == 0:
            #     # res = 'A' + res
            #     break
            n /= 26
        return res

s = Solution()
num = 52

print s.convertToTitle(num)