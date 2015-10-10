__author__ = 'keleigong'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        stack = [root]
        tmp = {root: 0}
        res = 0
        while len(stack) > 0:
            node = stack.pop()
            res = tmp[node] + node.val
            if node.right:
                stack.append(node.right)
                tmp[node.right] = res
            if node.left:
                stack.append(node.left)
                tmp[node.left] = res
            if node.left is None and node.right is None:
                if res == sum:
                    return True
        return False


