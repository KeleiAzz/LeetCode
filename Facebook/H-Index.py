class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) == 0:
            return 0
        citations.sort()
        return self.binSearch(citations, 0, len(citations) - 1)

    def binSearch(self, nums, start, end):
        if start == end:
            if nums[start] >= len(nums) - start:
                return len(nums) - start
            return 0
        if end - start == 1:
            if nums[start] >= len(nums) - start:
                return len(nums) - start
            elif nums[end] >= len(nums) - end:
                return len(nums) - end
            else:
                return 0
        mid = (start + end) / 2
        if nums[mid] == len(nums) - mid:
            return len(nums) - mid
        elif nums[mid] > len(nums) - mid:
            # if mid > 0 and nums[mid-1] == len(nums) - mid + 1:
            #     return nums[mid-1]
            if mid > 0 and nums[mid-1] < len(nums) - mid + 1:
                return len(nums) - mid
            return self.binSearch(nums, start, mid - 1)
        else:
            return self.binSearch(nums, mid + 1, end)
        # for i in range(1, len(citations) + 1):
        #     num = len(filter(lambda x: x >= i, citations))
        #     if num > i:
        #         continue
        #     elif num == i:
        #         return i
        #     else:
        #         return i - 1
        # return 0