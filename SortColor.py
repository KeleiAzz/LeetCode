__author__ = 'keleigong'
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        red = 0
        blue = -1
        i = 0
        print len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = nums[red]
                nums[red] = 0
                red += 1
                # print nums
        i = red
        # for i in range()
        while i < len(nums):
            if nums[i] == 2:
                nums[i] = nums[blue]
                nums[blue] = 2
                blue -= 1
            if nums[i] != 2:
                i += 1
            # print nums, i, blue
            if i == len(nums) + blue + 1:
                break
s = Solution()
s.sortColors([0,2,1,2,1,1,2,0,0,1,0])