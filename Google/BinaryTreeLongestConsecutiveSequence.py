# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0
        def dfs(root):
            l = dfs(root.left) + 1 if root.left else 1
            if root.left and root.left.val - root.val != 1:
                l = 1
            r = dfs(root.right) + 1 if root.right else 1
            if root.right and root.right.val - root.val != 1:
                r = 1
            self.longest = max(l, r, self.longest)
            return max(l, r)
        if root:
            dfs(root)
        return self.longest