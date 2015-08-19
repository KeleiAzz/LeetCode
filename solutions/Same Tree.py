__author__ = 'keleigong'

class Solution:
    def isSameTree(self, p, q):
        try:
            if p.val == q.val:
                return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)
            else:
                return False
        except AttributeError:
            if p != q:
                return False
        return True
