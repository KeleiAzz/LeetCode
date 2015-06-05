__author__ = 'keleigong'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        mi = min(nums)
        if mi < 0:
            for i in range(len(nums)):
                nums[i] += abs(mi)
        l = max(nums) + 1
        a = [0] * l
        for i in nums:
            if a[i] == 0:
                a[i] = i
            else:
                a[i] = 0
        if mi < 0:
            return sum(a) - abs(mi)
        else:
            return sum(a)


nums = [1,1,3,3,4,4,5,5,6,6,7,-10,-10,-3,7,]

s = Solution()

print s.singleNumber(nums)