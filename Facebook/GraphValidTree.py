from collections import defaultdict
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) == 0 and n == 1:
            return True
        elif len(edges) == 0:
            return False
        d = defaultdict(list)
        for edge in edges:
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
        visited = set()
        stack = [edges[0][0]]
        while len(stack) > 0:
            print stack
            node = stack.pop()
            if node in visited:
                print 'here'
                return False
            else:
                visited.add(node)
                for v in d[node]:
                    if v not in visited:
                        stack.append(v)

        if len(visited) == n:
            return True
        return False

edges = [[0, 1], [1, 4], [2, 3], [1, 2], [1, 3]]
s = Solution()
print s.validTree(5, edges)