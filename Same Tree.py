__author__ = 'keleigong'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        queue_p = [p]
        queue_q = [q]
        while queue_p:
            nd_p = queue_p.pop(0)
            nd_q = queue_q.pop(0)
            if nd_p.val != nd_q.val:
                return False
            if nd_p.left is not None and nd_q.left is not None:
                queue_p.append(nd_p.left)
                queue_q.append(nd_q.left)
                if nd_p.left.val != nd_q.left.val:
                    return False
            elif nd_p.left is None and nd_q.left is None:
                pass
            else:
                return False
            if nd_p.right is not None and nd_q.right is not None:
                queue_p.append(nd_p.right)
                queue_q.append(nd_q.right)
                if nd_p.right.val != nd_q.right.val:
                    return False
            elif nd_p.right is None and nd_q.right is None:
                pass
            else:
                return False
        return True