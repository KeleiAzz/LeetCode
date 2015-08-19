__author__ = 'keleigong'
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        # if len(nums) == 2:
        #     return max(max(nums), sum(nums))
        row = [0] * len(nums)
        res = [row] * len(nums)

