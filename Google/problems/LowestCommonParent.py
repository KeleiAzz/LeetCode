class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getLowestCommonParent(root, p, q):
    '''
    not correct here
    :param root:
    :param p:
    :param q:
    :return:
    '''
    if not root:
        return None
    if root.left == p or root.right == p or root.left == q or root.right == q:
        return root
    left = getLowestCommonParent(root.left, p, q)
    right = getLowestCommonParent(root.right, p, q)
    if left is not None and right is not None:
        return root
    if left:
        return left
    else:
        return right

root =TreeNode(50)
root.left =TreeNode(10)
root.right = TreeNode(60)
root.left.left = TreeNode(5)
root.left.right = TreeNode(20)
root.right.left = TreeNode(55)
root.right.left.left = TreeNode(45)
root.right.right = TreeNode(70)
root.right.right.left = TreeNode(65)
root.right.right.right = TreeNode(80)


print getLowestCommonParent(root, root.left.left, root.left.right).val