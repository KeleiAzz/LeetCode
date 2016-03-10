# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        nums = self.inorder(root)
        res = nums[:k]
        for i in range(k, len(nums)):
            if abs(res[0] - target) > abs(nums[i] - target):
                res.append(nums[i])
                res.pop(0)
            else:
                return res
        return res


    def inorder(self, root):
        res = []
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res