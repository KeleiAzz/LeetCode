# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.createTrees(1, n)

    def createTrees(self, start, end):
        if start > end:
            return [None]
        res = []
        for i in range(start, end+1):
            left = self.createTrees(start, i-1)
            right = self.createTrees(i+1, end)
            all_case = ((l, r) for l in left for r in right)
            for case in all_case:
                node = TreeNode(i)
                node.left = case[0]
                node.right = case[1]
                res.append(node)
        return res