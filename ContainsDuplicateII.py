__author__ = 'keleigong'
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        tmp = [i for i in nums]
        tmp.sort()
        dup = {}
        for i in range(len(tmp) - 1):
            if tmp[i] == tmp[i+1]:
                dup[tmp[i]] = []
        for i in range(len(nums)):
            if nums[i] in dup.keys():
                dup[nums[i]].append(i)

        for num in dup.keys():
            for i in range(len(dup[num]) - 1):
                if dup[num][i + 1] - dup[num][i] <= k:
                    return True
        return False
s = Solution()

nums = [1,2,3,1,2,3]
k = 2
print s.containsNearbyDuplicate(nums, k)