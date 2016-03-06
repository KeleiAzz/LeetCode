class Solution:
    # @param heights: a list of integers
    # @return: an integer
    def maxArea(self, heights):
        # write your code here
        if not heights:
            return 0

        left, right = 0, len(heights) - 1
        res = 0
        while left < right:
            if heights[left] >= heights[right]:
                res = max(res, (right - left) * heights[right])
                right -= 1
            else:
                res = max(res, (right - left) * heights[left])
                left += 1
        return res
