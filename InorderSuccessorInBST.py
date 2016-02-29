# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        node = root
        stack = []
        flag = 0
        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                if len(stack) > 0:
                    node = stack.pop()
                    if flag == 1:
                        return node
                    if node == p:
                        flag = 1
                    node = node.right
                else:
                    return None


        