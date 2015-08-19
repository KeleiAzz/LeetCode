__author__ = 'keleigong'
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        queue = []
        depth = {}
        if root is not None:
            depth[root] = 0
            queue.append(root)
        while queue:
            nd = queue.pop(0)
            if len(queue)>0 and depth[queue[0]] == depth[nd]:
                nd.next = queue[0]
            else:
                nd.next = None
            if nd.left:
                depth[nd.right] = depth[nd] + 1
                depth[nd.left] = depth[nd] + 1
                queue.append(nd.left)
                queue.append(nd.right)
