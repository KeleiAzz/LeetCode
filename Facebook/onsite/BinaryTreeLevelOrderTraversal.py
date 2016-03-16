# from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    DFS
    '''
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        return res

    def levelOrder2(self, root):
        '''
        BFS
        :param root:
        :return:
        '''
        if not root:
            return []
        res = []
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return res

    def levelOrder3(self, root):
        '''
        Recursive
        :param root:
        :return:
        '''
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