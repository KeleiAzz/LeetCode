__author__ = 'keleigong'
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def build(nums):
            if len(nums) == 0:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            if len(nums) % 2 == 1:
                mid = len(nums) / 2
            else:
                mid = len(nums) / 2 - 1
            root = TreeNode(nums[mid])
            root.left = build(nums[0:mid])
            root.right = build(nums[mid+1:])
            return root
        return build(nums)
