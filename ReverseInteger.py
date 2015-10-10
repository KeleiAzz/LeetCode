__author__ = 'keleigong'
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if abs(x) < 10:
            return x
        else:
            if x < 0:
                neg = -1
            else:
                neg = 1
            digits = []
            x = abs(x)
            while x >= 10:
                digit = x % 10
                digits.append(digit)
                x -= digit
                x /= 10
            digits.append(x)
        j = 0
        res = 0
        for i in reversed(digits):
            res += i * (10 ** j)
            j += 1
        if res > 2 ** 31:
            return 0
        return res * neg