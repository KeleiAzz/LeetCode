class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums) - 1
        start, end = -1, -1
        while l <= r:
            m = (l + r) / 2
            print l, m, r
            if nums[m] == target:
                if m > 0 and nums[m-1] == target:
                    r = m - 1
                else:
                    start = m
                    break
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        if start == -1:
            return [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if nums[m] == target:
                if m < len(nums) - 1 and nums[m+1] == target:
                    l = m + 1
                else:
                    end = m
                    break
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return [start, end]


nums = [5, 7, 7, 8, 8, 10]
s = Solution()
print s.searchRange(nums, 8)