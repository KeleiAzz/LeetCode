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
        pre, prepre = max(nums[1], nums[0]), nums[0]
        tmp = pre
        for i in range(2, len(nums)):
            tmp = max(prepre + nums[i], pre)
            prepre, pre = pre, tmp
        return tmp

s = Solution()
t = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
print s.rob(t)