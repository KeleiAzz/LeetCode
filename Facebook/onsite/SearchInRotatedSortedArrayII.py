class Solution(object):
    def search(self, nums, target):
        """
        The most important thing is to make nums[low] != nums[high]
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low = 0
        high = len(nums) - 1
        while nums[low] == nums[high] and high > 0:
            high -= 1

        while low <= high:
            mid = low + high >> 1
            if nums[mid] == target:
                return True
            if (target < nums[0] and not target < nums[mid] < nums[0]) or \
                    (target >= nums[0] and nums[0] <= nums[mid] < target):
                low = mid + 1
            else:
                high = mid - 1
        return False