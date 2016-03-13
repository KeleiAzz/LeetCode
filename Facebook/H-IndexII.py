class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0
        return self.binSearch(citations, 0, len(citations) - 1 )

    def binSearch(self, nums, start, end):
        if start > end:
            return len(nums) - start

        mid = (start + end) / 2
        if nums[mid] == len(nums) - mid:
            return len(nums) - mid
        elif nums[mid] > len(nums) - mid:
            return self.binSearch(nums, start, mid-1)
        else:
            return self.binSearch(nums, mid + 1, end)