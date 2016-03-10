class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict(zip(nums, [1] * len(nums)))
        # stack = []
        res = 0
        while len(nums) > 0:
            stack = [nums.pop()]
            if d[stack[0]] == 0:
                continue
            length = 0
            while len(stack) > 0:
                tmp = stack.pop()
                length += 1
                d[tmp] = 0
                if d.get(tmp+1, 0):
                    stack.append(tmp+1)
                if d.get(tmp-1, 0):
                    stack.append(tmp-1)
            res = max(res, length)
        return res
