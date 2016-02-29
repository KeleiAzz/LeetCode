class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        count = 1
        res = 1
        prev = nums[0]
        ptr = 1
        while ptr < len(nums):
            if count < 2 and nums[ptr] == prev:
                res += 1
                count += 1
                ptr += 1
            elif count >= 2 and nums[ptr] == prev:
                nums.pop(ptr)
            else:
                res += 1
                count = 1
                prev = nums[ptr]
                ptr += 1
        return res
