class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n <= 1:
            return 1
        p = [-1] * len(primes)
        v = [1] * len(primes)
        dp = [1] * n
        # x = 1
        for k in range(n):
            x = min(v)
            dp[k] = x
            for i, val in enumerate(v):
                if x == val:
                    p[i] += 1
                    v[i] = dp[p[i]] * primes[i]
        return dp[-1]
        