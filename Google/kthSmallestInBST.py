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
        # count = 0
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
        return None


    def kthSmallest2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None
        def helper(node):
            if not node:
                return
            helper(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            helper(node.right)
        helper(root)
        return self.res

