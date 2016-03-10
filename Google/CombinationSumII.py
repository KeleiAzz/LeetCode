class Solution(object):
    cache = {}
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        i = 0
        while i < len(candidates):
            if candidates[i] == target:
                res.append([target])
            elif candidates[i] > target:
                break
            else:
                tmp = self.combinationSum2(candidates[i+1:], target - candidates[i])
                for l in tmp:
                    # if l:
                    res.append([candidates[i]]+l)
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            i += 1
        return res
