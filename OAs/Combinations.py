class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if not n or not k:
            return []
        nums = range(1, n+1)
        return self.helper(nums, k)

    def helper(self, nums, k):
        if not nums or not k:
            return []
        if k == 1:
            return [[i] for i in nums]
        res = []
        # nums = range(1, n+1)
        for i in range(len(nums)-k+1):
            tmp = self.helper(nums[i+1:], k-1)
            for l in tmp:
                res.append([nums[i]] + l)

        return res


s = Solution()
print s.combine(10, 3)