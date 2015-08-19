__author__ = 'keleigong'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}

    def preorderTraversal(self, root):
        if root is None:
            return []
        val = []
        val.append(root.val)
        if root.left is not None:
            val += self.preorderTraversal(root.left)
        if root.right is not None:
            #val.append[root.right.val]
            val += self.preorderTraversal(root.right)
        return val
