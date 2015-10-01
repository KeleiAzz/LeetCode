__author__ = 'keleigong'
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        while(1):
            try:
                nums.remove(0)
                i += 1
            except:
                break
        return nums + [0] * i


s = Solution()

print s.moveZeroes([1, 2, 3, 5])