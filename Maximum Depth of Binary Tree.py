__author__ = 'keleigong'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        queue = [root]
        tree_depth = {root: 1}
        cur_depth = 0
        while queue:
            nd = queue.pop(0)
            #if nd in tree_depth.keys():
            cur_depth = tree_depth[nd]
            #else:
            if nd.left is not None:
                tree_depth[nd.left] = cur_depth + 1
                queue.append(nd.left)
            if nd.right is not None:
                tree_depth[nd.right] = cur_depth + 1
                queue.append(nd.right)
        return max(tree_depth.itervalues())

