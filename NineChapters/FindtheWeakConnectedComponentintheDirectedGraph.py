# Definition for a directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    '''
    Use the thought of union find, if the ancestors of two nodes are different,
    point one of the ancestor to another.
    After the traversal, find every node's ancestor.
    '''
    # @param {DirectedGraphNode[]} nodes a array of directed graph node
    # @return {int[][]} a connected set of a directed graph
    def connectedSet2(self, nodes):
        # Write your code here
        find = dict()
        for node in nodes:
            find[node] = node
        for node in nodes:
            for neighbor in node.neighbors:
                fnode = self.findAnc(node, find)
                find[node] = fnode
                fneighbor = self.findAnc(neighbor, find)
                find[neighbor] = fneighbor
                if fnode != fneighbor:
                    find[fnode] = find[fneighbor]
                    find[node] = fneighbor
        res = {}
        for key in find.keys():
            father = self.findAnc(key, find)
            if father not in res:
                res[father] = [key]
            else:
                res[father].append(key)
        res = res.values()
        for i in range(len(res)):
            res[i] = [x.label for x in res[i]]
            res[i].sort()
        return res

    def findAnc(self, node, find):
        father = find[node]
        while father != find[father]:
            father = find[father]
        return father