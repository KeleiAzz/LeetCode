class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.binSearch(nums, 0, len(nums) - 1)


    def binSearch(self, nums, low, high):
        if low >= high:
            return low
        mid = low + high >> 1
        if nums[mid] < nums[mid+1]:
            return self.binSearch(nums, mid + 1, high)
        else:
            return self.binSearch(nums, low, mid)