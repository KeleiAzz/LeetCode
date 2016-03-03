class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if not n:
            return 0
        find = range(n)
        count = n
        for i, j in edges:
            fi = self.findAnce(find, i)
            fj = self.findAnce(find, j)
            if fi != fj:
                find[fj] = fi
                find[j] = fi
                find[i] = fi
                count -= 1
            else:
                find[fj] = fi
                find[j] = fi
                find[i] = fi
        return count



    def findAnce(self, find, node):
        father = find[node]
        while father != find[father]:
            father = find[father]
        return father