# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def allPath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        path = []
        res = []
        stack = [(root, 0)]
        flag = -1
        while stack:
            node, level = stack.pop()
            if flag >= 0:
                for i in range(flag - level + 1):
                    path.pop()
                flag = -1
            path.append(node.val)
            if node.left is None and node.right is None:
                res.append(path[:])
                flag = level
            else:
                if node.right:
                    stack.append((node.right, level + 1))
                if node.left:
                    stack.append((node.left, level + 1))
        return res

a = TreeNode(0)
b = TreeNode(1)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(5)
g = TreeNode(6)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
c.right = g

s = Solution()
print s.allPath(a)
