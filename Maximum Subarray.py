class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        a = [0]*len(nums)
        a[0] = nums[0]
        res = a[0]
        for i in range(1,len(nums)):
            a[i] = max(a[i-1] + nums[i], nums[i])
            res = max(res, a[i])
                
        return res