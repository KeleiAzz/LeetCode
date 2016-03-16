# TODO solve it with union find
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


    def longestConsecutive2(self, nums):
        """
        using set
        :type nums: List[int]
        :rtype: int
        """
        d = set(nums)
        res = 0
        while nums:
            stack = [nums.pop()]
            if stack[0] not in d:
                continue
            count = 0
            while stack:
                n = stack.pop()
                count += 1
                # d[n] = 0
                d.remove(n)
                if n + 1 in d:
                    stack.append(n+1)
                if n - 1 in d:
                    stack.append(n-1)
            res = max(res, count)
        return res