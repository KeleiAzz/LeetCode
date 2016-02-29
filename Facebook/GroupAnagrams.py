from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            return []
        if len(strs) == 1:
            return [strs]

        res = defaultdict(list)
        for word in strs:
            tmp = ''.join(sorted(list(word)))
            res[tmp].append(word)
        return [sorted(x) for x in res.values()]