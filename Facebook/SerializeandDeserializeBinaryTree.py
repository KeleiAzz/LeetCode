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
        if not root:
            return []
        queue = [root]
        l = [map(queue.append, (node.left, node.right)) for node in queue if node]
        return ':'.join(map(lambda n: n and str(n.val) or 'x', queue))

        # res = []
        #
        # queue = [root]
        # while len(queue) > 0:
        #     node = queue.pop(0)
        #     if node:
        #         res.append(str(node.val))
        #         queue.append(node.left)
        #         queue.append(node.right)
        #     else:
        #         res.append('x')
        # return ':'.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        data = data.split(':')
        root = TreeNode(data[0])
        queue = [root]
        count = 2
        for i in range(1, len(data), 2):
            node = queue.pop(0)
            l = data[i]
            if l != 'x':
                left = TreeNode(l)
                node.left = left
                queue.append(left)
            r = data[i+1]
            if r != 'x':
                right = TreeNode(r)
                node.right = right
                queue.append(right)
        return root
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))