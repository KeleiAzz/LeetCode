# coding=utf-8
class Solution(object):
    def findMin(self, nums):
        """
        二分查找还是总容易出问题.
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] >= nums[lo] and nums[mid] >= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
        return nums[lo]


    def findMin2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[hi] > nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]

