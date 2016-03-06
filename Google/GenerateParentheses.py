class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(path, left, right, n):
            if left < right or left > n or right > n:
                return
            if len(path) == n * 2:
                res.append(path)
                return
            dfs(path+'(', left+1, right, n)
            dfs(path+')', left, right+1, n)

        dfs('', 0, 0, n)
        return res


s = Solution()
print s.generateParenthesis(4)