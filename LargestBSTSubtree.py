# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = [root]
        node = None
        largest = 0
        while len(queue) > 0:
            node = queue.pop(0)
            size = self.isBST(node)
            if size >= largest:
                largest = size
            elif size < 0:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return largest

    def isBST(self, root):
        if root is None:
            return 0
        node = root
        while node.left is not None:
            node = node.left
        smaller = node.val - 1
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
                    if node.val > smaller:
                        smaller = node.val
                        count += 1
                        node = node.right
                    else:
                        return -1
                else:
                    return count