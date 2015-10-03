__author__ = 'keleigong'
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [str(i) for i in digits]
        num = int(''.join(digits))
        num += 1

        return [int(x) for x in list(str(num))]
