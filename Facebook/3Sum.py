from collections import Counter
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i, N, res = 0, len(nums) - 1, []
        while i <= N - 2:
            if nums[i] > 0:
                break
            j, k = i + 1, N
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    j += 1
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    k -= 1
                elif s < 0:
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    j += 1
                else:
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    k -= 1
            while i < N - 2 and nums[i] == nums[i + 1]: i += 1
            i += 1
        return res