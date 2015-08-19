__author__ = 'keleigong'
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        count = 1
        pre = nums[0]
        for i in nums[1:]:
            if i == pre:
                count += 1
            else:
                count -= 1
                if count <= 0:
                    pre = i
                    count = 1
        return pre

s = Solution()

print(s.majorityElement([1,2,3,1,1,]))