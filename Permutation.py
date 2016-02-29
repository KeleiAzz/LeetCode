__author__ = 'keleigong'
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]
        def get_permute(lists, num):
            res = []
            for list in lists:
                for i in range(len(list) + 1):
                    tmp = [x for x in list]
                    tmp.insert(i, num)
                    res.append(tmp)
            return res
        lists = [[nums[0], nums[1]], [nums[1], nums[0]]]
        # print get_permute(lists, 3)
        if len(nums) > 2:
            for i in range(2, len(nums), 1):
                lists = get_permute(lists, nums[i])
        return lists


s = Solution()

print s.permute([1,2,3,4])
