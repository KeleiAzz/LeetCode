__author__ = 'keleigong'
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        nums = [2 ** i for i in range(n)]
        s = 0
        i = 0
        while True:
            if len(res) == 2 ** n:
                break
            if s ^ nums[i] in res:
                i += 1
                pass
            else:
                res.append(s ^ nums[i])
                s = res[-1]
                i = 0
        return res