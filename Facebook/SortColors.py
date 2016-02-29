class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r = 0
        b = len(nums) - 1
        p = 0
        while p <= b:
            if nums[p] == 0:
                nums[p], nums[r] = nums[r], nums[p]
                r += 1
                p += 1
            elif nums[p] == 1:
                p += 1
            else:
                nums[p], nums[b] = nums[b], nums[p]
                # p += 1
                b -= 1
