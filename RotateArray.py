__author__ = 'keleigong'
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k > len(nums):
            k -= len(nums)
        saved = nums[-k:]
        for i in range(len(nums) - k - 1, -1, -1):
            nums[i+k] = nums[i]
        nums[0:k] = saved
        return nums

s = Solution()

l = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print s.rotate(l, 10)