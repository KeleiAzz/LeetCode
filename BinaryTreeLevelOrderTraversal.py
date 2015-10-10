__author__ = 'keleigong'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        def getNext(nodes):
            res = []
            for node in nodes:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
            # if len(res) == 0:
            #     return None
            return res
        res = []
        nodes = [root]
        while len(nodes) > 0:
            tmp = []
            for node in nodes:
                tmp.append(node.val)
            res.append(tmp)
            nodes = getNext(nodes)
        return res
