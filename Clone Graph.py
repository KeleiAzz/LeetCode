# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        #res = UndirectedGraphNode(node.label, [])
        if node is None:
            return None
        cloned = {}
        queue = [node]
        while queue:
            out = queue.pop(0)
            if not cloned.has_key(out.label):
                res = UndirectedGraphNode(out.label)
                cloned[out.label] = res
            else:
                res = cloned[out.label]
            
            for i in out.neighbors:
                if not cloned.has_key(i.label):
                    queue.append(i)
                    temp = UndirectedGraphNode(i.label)
                    cloned[i.label] = temp
                    res.neighbors.append(temp)
                else:
                    res.neighbors.append(cloned[i.label])
        return cloned[node.label]
            