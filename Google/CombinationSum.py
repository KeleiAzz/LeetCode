class Solution(object):
    cache = {}
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfs(candidates, [], res, target)
        return res

    def dfs(self, candidates, path, res, target):
        if target < candidates[0]:
            return
        # from large values to small values
        for i in range(len(candidates)):
            # if equal, it is one solution
            if candidates[i]==target:
                res.insert(0,path+[candidates[i]])
            # if smaller, try it and keep searching for candidates that are smaller
            # candidates[:i+1] to avoid duplicates
            elif candidates[i]<target:
                self.dfs(candidates[i:], path+[candidates[i]], res, target-candidates[i])
            # if larger, do nothing
