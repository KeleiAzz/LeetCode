__author__ = 'keleigong'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def get_depth(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            if node.left:
                left = get_depth(node.left)
            else:
                left = 0
            if node.right:
                right = get_depth(node.right)
            else:
                right = 0
            if left is None or right is None:
                return None
            if abs(left - right) > 1:
                return None
            return 1 + max(left, right)
        if get_depth(root) is None:
            return False
        else:
            return True

