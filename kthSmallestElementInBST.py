# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        node = root
        stack = []
        count = 0
        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                if len(stack) > 0:
                    node = stack.pop()
                    count += 1
                    if count == k:
                        return node.val
                    node = node.right
                else:
                    return None

