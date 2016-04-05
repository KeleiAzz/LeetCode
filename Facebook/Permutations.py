class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        # if len(nums) == 2:
        #     return [[nums[0], nums[1]], [nums[1], nums[0]]]

        res = []
        for i in range(len(nums)):
            tmp = self.permute(nums[:i] + nums[i+1:])
            for t in tmp:
                # print [nums[i]] + t
                res.append([nums[i]] + t)
        return res

s = Solution()
print s.permute([1,2,3,4])