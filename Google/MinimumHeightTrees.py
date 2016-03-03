from collections import defaultdict
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        d = defaultdict(set)
        for i, j in edges:
            d[i].add(j)
            d[j].add(i)
        leaves = list(set(i for i in d if len(d[i]) == 1))
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = d[i].pop()
                d[j].remove(i)
                if len(d[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves
