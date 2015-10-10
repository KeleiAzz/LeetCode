__author__ = 'keleigong'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        def getNext(nodes):
            res = []
            for node in nodes:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                if node.left is None and node.right is None:
                    return None
            return res
        nodes = [root]
        d = 0
        while nodes:
            d += 1
            nodes = getNext(nodes)
        return d
