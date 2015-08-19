__author__ = 'keleigong'
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        nums = sorted(nums)
        while True:
            tmp = nums[0]
            for j in range(3):
                try:
                    if tmp != nums.pop(0):
                        return tmp
                except:
                    return tmp


s = Solution()

a = [1]

print(s.singleNumber(a))