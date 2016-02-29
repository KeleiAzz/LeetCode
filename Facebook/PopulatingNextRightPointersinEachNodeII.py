# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root is None:
            return
        queue = [root]
        nxt = 0
        cur = 1
        prev_node = None
        flag = 0
        while len(queue) > 0:
            node = queue.pop(0)
            if flag != 1 and prev_node is not None:
                node.next = prev_node
                # flag = 0
            flag = 0
            prev_node = node
            cur -= 1
            if node.right:
                queue.append(node.right)
                nxt += 1
            if node.left:
                queue.append(node.left)
                nxt += 1
            if cur == 0:
                cur = nxt
                nxt = 0
                flag = 1
