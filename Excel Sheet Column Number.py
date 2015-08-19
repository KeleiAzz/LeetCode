__author__ = 'keleigong'
class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num = 0
        s = list(reversed(s))
        for i in range(len(s)):
            num += (letters.index(s[i]) + 1) *  (26**(i))
        return num