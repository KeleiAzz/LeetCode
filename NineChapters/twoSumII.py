class Solution:
    # @param nums, an array of integer
    # @param target, an integer
    # @return an integer
    def twoSum2(self, nums, target):
        # Write your code here
        res = 0
        nums.sort()
        j = len(nums) - 1
        i = 0
        while i < j:
            if nums[i] + nums[j] > target:
                res += j - i
                j -= 1
            else:
                i += 1
        return res
