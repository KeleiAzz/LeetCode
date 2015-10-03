__author__ = 'keleigong'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        def get_next_layer(nodes):
            res = []
            for node in nodes:
                if node:
                    res.append(node.left)
                    res.append(node.right)
                else:
                    res.append(None)
                    res.append(None)
            if all(i is None for i in res):
                return None
            return res
        layer = [root]
        while True:
            layer = get_next_layer(layer)
            if layer == None:
                return True
            nums = [node.val for node in layer]
            left = nums[0:len(nums)/2]
            right = nums[len(nums)/2:]
            right.reverse()
            if left != right:
                return False
