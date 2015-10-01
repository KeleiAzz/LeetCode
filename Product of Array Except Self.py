__author__ = 'keleigong'
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        n_0 = nums.count(0)
        if n_0 > 1:
            return [0] * len(nums)
        else:
            s = 1
            for i in nums:
                if i != 0:
                    s *= i
            if n_0 == 1:
                res = [0] * len(nums)
                res[nums.index(0)] = s
            else:
                res = []
                for i in nums:
                    if i == 0:
                        res.append(s)
                    else:
                        res.append(s/i)
        return res