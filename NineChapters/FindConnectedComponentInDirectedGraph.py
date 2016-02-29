# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        # Write your code here
        if not nodes:
            return []
        res = []
        visited = set()
        for node in nodes:
            if node not in visited:
                tmp = []
                queue = [node]
                visited.add(node)
                while queue:
                    n = queue.pop(0)
                    tmp.append(n)
                    # visited.add(n)
                    for neighbor in n.neighbors:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
                res.append(tmp)
        for i in range(len(res)):
            res[i] = [node.label for node in res[i]]
            res[i].sort()
        return res

