class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        acc = [0] * len(nums)
        acc[0] = nums[0]
        for i in range(1, len(nums)):
            acc[i] = acc[i-1] + nums[i]
        d = dict()
        for i, v in enumerate(acc): # there may be 0 in nums, so two adjacent value in acc may be identical
            if v not in d:
                d[v] = i
        max_length = 0
        for i in range(len(acc)):
            if acc[i] == k:
                max_length = max(max_length, i + 1)
            elif acc[i] - k in d:
                max_length = max(max_length, i - d[acc[i]-k])
        return max_length

s = Solution()

n = [-2,-1,2,1]

print s.maxSubArrayLen(n, 1)