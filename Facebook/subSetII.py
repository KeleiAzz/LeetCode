class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        self.dfs(sorted(nums), 0, '', res)
        res = list(set(res))
        res = [map(int, x[1:].split('#')) for x in iter(res) if x != '']
        res.append([])
        return res

    def dfs(self, nums, start, path, res):
        res.append(path)
        for i in range(start,len(nums)):
            self.dfs(nums, i+1, path + '#' +str(nums[i]), res)