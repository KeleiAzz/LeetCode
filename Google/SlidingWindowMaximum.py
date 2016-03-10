class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        win = nums[:k]
        # stack = [max(win)]
        stack = nums[:k]
        stack.sort(reverse=True)
        res = [stack[0]]
        for i in range(len(nums) - k):
            print stack
            head = nums[i]
            tail = nums[i+k]
            while stack and head == stack[0]:
                stack.pop(0)
            # stack.append(head)
            while stack and tail > stack[-1]:
                stack.pop()
            stack.append(tail)
            res.append(stack[0])
        return res

s = Solution()

print s.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5)