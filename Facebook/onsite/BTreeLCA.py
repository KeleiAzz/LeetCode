# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        use reach node to check if one node is another node's ancestor.
        if left can reach both, than the LCA must in the left subtree, same thing to the right.
        If both left and right can not reach both node, then the LCA should be the root.
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

    def reachNode(self, root, p):
        if root is None:
            return False
        if root == p:
            return True
        if self.reachNode(root.left, p) or self.reachNode(root.right, p):
            return True
        return False

    def lowestCommonAncestor2(self, root, p, q):
        """
        Using dfs in one pass. o(n)
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.shallowest = 0
        self.getFirstTarget = False
        self.tmpLCA, self.LCA = None, None
        def dfs(root, p, q, curLev):
            # global shallowest, getFirstTarget, tmpLCA, LCA
            if root == p or root == q:
                if not self.getFirstTarget:
                    self.getFirstTarget = True
                    self.shallowest = curLev
                    self.tmpLCA = root
                self.LCA = self.tmpLCA
            if self.getFirstTarget and curLev <= self.shallowest:
                self.shallowest = curLev
                self.tmpLCA = root

            if root.left is not None:
                dfs(root.left, p, q, curLev + 1)
                if self.getFirstTarget and curLev <= self.shallowest:
                    self.shallowest = curLev
                    self.tmpLCA = root

            if root.right is not None:
                dfs(root.right, p, q, curLev + 1)
                if self.getFirstTarget and curLev <= self.shallowest:
                    self.shallowest = curLev
                    self.tmpLCA = root
        if root is None:
            return root
        dfs(root, p, q, 0)
        return self.LCA

