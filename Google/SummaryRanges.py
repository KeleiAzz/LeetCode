class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        i, j = 0, 0
        res = []
        while i < len(nums) and j < len(nums) - 1:
            while j < len(nums) - 1 and nums[j+1] - nums[j] == 1:
                j += 1
            if j > i:
                res.append(str(nums[i]) + '->' + str(nums[j]))
                j += 1
                i = j
            else:
                res.append(str(nums[i]))
                j += 1
                i += 1

        if j == i < len(nums):
            res.append(str(nums[i]))
        return res