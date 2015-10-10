__author__ = 'keleigong'
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        elif len(nums) == 3:
            return max(nums[1], nums[0] + nums[2])
        else:
            a = nums[0] + self.rob(nums[2:])
            b = self.rob(nums[1:])
            return max(a, b)

s = Solution()
t = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
print s.rob(t)