# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or (root == p or root == q):
            return root
        if self.reachNode(p, q):
            return p
        if self.reachNode(q, p):
            return q

        if self.reachNode(root.left, p) and self.reachNode(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        elif self.reachNode(root.right, p) and self.reachNode(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def reachNode(self,root, p):
        if root is None:
            return False
        if root == p:
            return True
        if root.left is None and root.right is None:
            return False
        if self.reachNode(root.left, p):
            return True
        if  self.reachNode(root.right, p):
            return True
        return False