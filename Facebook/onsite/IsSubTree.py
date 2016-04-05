def isSub(root1, root2):
    if sameTree(root1, root2):
        return True
    else:
        return isSub(root1.left, root2) or isSub(root1.right, root2)


def sameTree(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    if root1.val == root2.val:
        return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)
    return False