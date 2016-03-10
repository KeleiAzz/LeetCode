from collections import defaultdict
class Solution(object):
    def levelOrder(self, root):
        result = []
        self.level_dfs(root, 0, result)
        return result

    def level_dfs(self, node, level, result):
        if not node:
            return
        if level == len(result):
            result.append([])
        result[level].append(node.val)
        self.level_dfs(node.left, level+1, result)
        self.level_dfs(node.right, level+1, result)

    def levelOrderBFS(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = defaultdict(list)
        if root is None:
            return []
        level = 0
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            res[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))

        return [res[i] for i in range(0, level+1)]

    def levelOrderByLevel(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res

        stack = [root]
        while stack:
            tmp = []
            values = []
            for node in stack:
                values.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            stack = tmp
            res.append(values)
        return res