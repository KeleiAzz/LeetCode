# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        node = root
        stack = []
        pre_node = None
        pre_diff = float('INF')
        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                if len(stack) > 0:
                    node = stack.pop()
                    # pre_node = node
                    if abs(node.val - target) > pre_diff:
                        return pre_node.val
                    else:
                        pre_diff = abs(node.val - target)
                        pre_node = node
                    node = node.right
                else:
                    return pre_node.val

