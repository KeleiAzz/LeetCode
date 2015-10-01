__author__ = 'keleigong'
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num <= 0:
            return False
        if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
            return False
        # else:
        #     return False
        while True:
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5
            else:
                break
        if num < 5:
            return True
        else:
            return False

