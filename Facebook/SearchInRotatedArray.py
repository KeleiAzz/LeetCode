class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + high >> 1
            if nums[mid] == target:
                return mid
            if (target < nums[0] and not target < nums[mid] < nums[0] or
                    target >= nums[0] and nums[0] <= nums[mid] < target):

                low = mid + 1
            else:
                high = mid - 1

        return -1


