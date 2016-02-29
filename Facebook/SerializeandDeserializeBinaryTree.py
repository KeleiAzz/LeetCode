# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)

a.left = b
a.right = c

queue = [a]

l = [map(queue.append, (node.left, node.right)) for node in queue if node]

print queue
print ':'.join(map(lambda n: n and str(n.val) or 'x', queue))

print a

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return []
        res = []
        node = root
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.extend([None])
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        root = TreeNode(data.pop(0))
        queue = [root]
        count = 2
        while len(data) > 0:
            node = queue.pop(0)
            l = data.pop(0)
            if l is not None:
                left = TreeNode(l)
                node.left = left
                queue.append(left)
            r = data.pop(0)
            if r is not None:
                right = TreeNode(r)
                node.right = right
                queue.append(right)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))