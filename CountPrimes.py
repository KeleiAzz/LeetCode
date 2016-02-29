__author__ = 'keleigong'
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        primes = [2]
        for i in range(3, n, 2):
            flag = 1
            for j in primes:
                if i % j == 0:
                    flag = 0
                    continue
            if flag is 1:
                primes.append(i)
        print primes
        return len(primes)

s = Solution()

print s.countPrimes(49997)