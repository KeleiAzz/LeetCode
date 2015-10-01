__author__ = 'keleigong'
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        DIGITS = {
            'I': 1,    'V': 5,    'X': 10,    'L': 50,
            'C': 100,  'D': 500,  'M': 1000,
        }
        s = list(s)
        s.reverse()
        num = 0
        prev = None
        for i in range(len(s) - 1):
            digit_value = DIGITS[s[i]]
            if prev and prev > digit_value:
                num -= digit_value
            else:
                num += digit_value
            prev = digit_value

        return num

s = Solution()

print s.romanToInt('XLIX')