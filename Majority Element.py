__author__ = 'keleigong'
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        nums = sorted(nums)
        return nums[len(nums)/2]