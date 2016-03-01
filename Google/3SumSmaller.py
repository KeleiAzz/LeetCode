class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        nums.sort()
        left = 0
        right = len(nums) -1
        count = 0
        while left < right - 1:
            mid = right -1
            while left < mid:
                if nums[left] + nums[mid] < target - nums[right]:
                    count += mid - left
                    left += 1
                else:
                    mid -= 1
            left = 0
            right -= 1
        return count