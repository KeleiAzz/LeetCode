__author__ = 'keleigong'
class Solution(object):
    def singleNumber(self, nums):
        # https://leetcode.com/discuss/48119/single-number-iii
        xor = 0
        for num in nums: xor ^= num
        xor = xor & (xor - 1) ^ xor
        a = b = 0
        for num in nums:
            if xor & num:
                a ^= num
            else:
                b ^= num
        return [a, b]

s = Solution()

print s.singleNumber([1,1,2,2,3,3,5,6,7,7,8,8,9,9])