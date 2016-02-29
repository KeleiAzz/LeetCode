__author__ = 'keleigong'
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i = 0
        left = 0
        res = []
        while i < len(nums) - 1:
            if nums[i+1] - nums[i] == 1:
                i += 1
                continue
            else:
                if left == i:
                    res.append(str(nums[i]))
                else:
                    res.append('%d->%d' % (nums[left], nums[i]))
                i += 1
                left = i
        if left == len(nums) - 1:
            res.append(str(nums[-1]))
        elif nums[-1] == nums[-2] + 1:
            res.append('%d->%d' % (nums[left], nums[-1]))
        else:
            res.append('%d->%d' % (nums[left], nums[-2]))
            res.append(str(nums[-1]))
        return res

s = Solution()

nums = [1]

print s.summaryRanges(nums)