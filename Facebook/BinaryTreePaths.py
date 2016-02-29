# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        else:
            paths = []
            self.createPath(root, str(root.val), paths)
            return paths

    def createPath(self, root, path, paths):
        if root.left is None and root.right is None:
            paths.append(path)
        if root.left:
            self.createPath(root.left, path + '->' + str(root.left.val), paths)
        if root.right:
            self.createPath(root.right, path + '->' + str(root.right.val), paths)