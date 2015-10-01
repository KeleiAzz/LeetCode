__author__ = 'keleigong'
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def factorial(n): return reduce(lambda x, y: x * y, [1] + range(1, n + 1, 1))

        def C(n, p):
            up = factorial(n)
            down = factorial(p) * factorial(n-p)
            return up/down
        if n == 1:
            return 1
        if n == 2:
            return 2
        res = 0
        if n % 2 == 0:
            for i in range(0, n+1, 2):
                res += C( i + (n - i)/2, i)
        else:
            for i in range(1, n + 1, 2):
                res += C(i + (n - i)/2, i)
        return res


s = Solution()

print s.climbStairs(5)