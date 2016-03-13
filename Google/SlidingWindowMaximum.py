class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        result = []
        q = []
        for i in range(len(nums)):
            while len(q) and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            # print q
            if i < k - 1:
                continue

            while len(q) and q[0] <= i - k:
                q.pop(0)

            result.append(nums[q[0]])

        return result
s = Solution()

print s.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5)