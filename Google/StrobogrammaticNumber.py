class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num:
            return True
        sym = ['1', '8', '0']
        if len(num) % 2 == 1:
            mid = len(num) / 2
            if num[mid] not in sym:
                return False
        tmp = num[::-1]
        for i in range(len(num)/2):
            if (num[i] == tmp[i] and num[i] in sym) or (num[i] == '6' and tmp[i] == '9') or \
            (num[i] == '9' and tmp[i] == '6'):
                pass
            else:
                return False
        return True