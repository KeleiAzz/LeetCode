__author__ = 'keleigong'
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = [-1] * (len(nums) + 1)
        for i in nums:
            x[i] = i

        return x.index(-1)