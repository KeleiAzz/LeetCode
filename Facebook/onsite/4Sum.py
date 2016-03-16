class Solution(object):
    def fourSum(self, nums, target):
        """
        Similar approach to 3sum, n^3 time complexity.
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        i = 0
        while i <= len(nums) - 4:
            if nums[i] * 4 > target:
                break
            j = len(nums) - 1
            while j > i + 2:
                left, right = i + 1, j - 1
                tmp_target = target - nums[i] - nums[j]
                while left < right:
                    tmp_sum = nums[left] + nums[right]
                    if tmp_sum == tmp_target:
                        res.append([nums[i], nums[left], nums[right], nums[j]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        left += 1
                        while right > left and nums[right] == nums[right-1]:
                            right -= 1
                        right -= 1
                    elif tmp_sum > tmp_target:
                        while right > left and nums[right] == nums[right-1]:
                            right -= 1
                        right -= 1
                    else:
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        left += 1
                while j > i + 2 and nums[j] == nums[j-1]:
                    j -= 1
                j -= 1
            while i <= len(nums) - 4 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res