# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.uniCount(root)[1]


    def uniCount(self, root):
        if root is None:
            return True, 0
        if root.left is None and root.right is None:
            return True, 1
        res = 0
        is_uni = 0
        left, left_count = self.uniCount(root.left)
        right, right_count = self.uniCount(root.right)
        res += left_count + right_count
        if left and right and (root.left is None or root.val == root.left.val) \
                          and (root.right is None or root.val == root.right.val):
            is_uni = 1
            res += 1
        if is_uni:
            return True, res
        else:
            return False, res

