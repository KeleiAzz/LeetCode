class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

max_depth = -1
def longestPath(root):
    res = []
    dfs(root, [], res, 0)
    print res
    return [path for path in res if len(path) == max_depth]

def dfs(root, path, res, depth):
    global max_depth
    if not root:
        return
    if root.left is None and root.right is None:
        if depth + 1 >= max_depth:
            res.append(path + [root])
            max_depth = depth + 1

    if root.left:
        dfs(root.left, path + [root], res, depth + 1)
    if root.right:
        dfs(root.right, path + [root], res, depth + 1)

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(8)
root.right.right.left.left = TreeNode(9)


print longestPath(root)