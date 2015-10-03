__author__ = 'keleigong'
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        tmp = nums[0]
        to_remove = []
        for i in range(1, len(nums), 1):
            if nums[i] == tmp:
                to_remove.append(i)
            else:
                tmp = nums[i]
        to_remove.reverse()
        for i in to_remove:
            nums.pop(i)

        return len(nums)
