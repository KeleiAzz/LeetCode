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
            j, mid = N, i + 1
            while mid < j:
                tmpSum = nums[i] + nums[mid] + nums[j]
                if tmpSum == 0:
                    res.append([nums[i], nums[mid], nums[j]])
                    while mid < j and nums[mid] == nums[mid+1]:
                        mid += 1
                    mid += 1
                    while j > mid and nums[j] == nums[j-1]:
                        j -= 1
                    j -= 1
                elif tmpSum > 0:
                    while j > mid and nums[j] == nums[j-1]:
                        j -= 1
                    j -= 1
                else:
                    while mid < j and nums[mid] == nums[mid+1]:
                        mid += 1
                    mid += 1
            while i <= N - 2 and nums[i] == nums[i+1]:
                i += 1
            i += 1
        return res
