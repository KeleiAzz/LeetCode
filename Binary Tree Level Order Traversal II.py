__author__ = 'keleigong'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def get_next(nodes):
            next_layer = []
            current = []
            for node in nodes:
                current.append(node.val)
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            if all(x is None for x in next_layer):
                return [nodes]
            # next_layer_val = [x.val for x in next_layer]
            # l.append(next_layer_val)
            return  get_next(next_layer) + [nodes]
        if root:
            l = get_next([root])
            res = []
            for li in l:
                res.append([])
                for node in li:
                    res[-1].append(node.val)
            return res
        else:
            return []
