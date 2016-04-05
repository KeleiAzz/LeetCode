class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        tmp = 1
        for j in range(n)[::-1]:
            res[j] *= tmp
            tmp *= nums[j]
        return res


a = [1, 2, 3, 4, 5, 6]
s = Solution()
print s.productExceptSelf(a)