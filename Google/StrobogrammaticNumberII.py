class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return 0
        res = set()
        if n % 2 == 0:
            leftHaves = self.formHalf(n / 2)
            for left in leftHaves:
                right = left[::-1]
                right = right.replace('6', '*')
                right = right.replace('9', '6')
                right = right.replace('*', '9')
                res.add(left + right)
        else:
            nums = ['1', '8', '0']
            leftHaves = self.formHalf(n / 2)
            for left in leftHaves:
                right = left[::-1]
                right = right.replace('6', '*')
                right = right.replace('9', '6')
                right = right.replace('*', '9')
                for num in nums:
                    res.add(left + num + right)
        return list(res)

    def formHalf(self, n):
        nums = ['1', '8', '0', '6', '9']
        res = []
        if n == 1:
            return nums
        for i in nums:
            tmp = self.formHalf(n - 1)
            for t in tmp:
                res.append(i+t)
        return res


s = Solution()
print s.findStrobogrammatic(5)