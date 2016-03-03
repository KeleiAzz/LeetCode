class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, start, path, res):
        res.append(path)
        for i in range(start,len(nums)):
            self.dfs(nums, i+1, path+[nums[i]],res)



s = Solution()
print s.subsets(range(4))