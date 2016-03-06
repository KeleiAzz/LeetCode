class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        if not heights:
            return 0
        res = 0
        left, right = 0, len(heights) - 1
        while left < right:
            if heights[left] <= heights[right]:
                smaller = heights[left]
                while left < right and heights[left] <= smaller:
                    res += smaller - heights[left]
                    left += 1
            else:
                smaller = heights[right]
                while left < right and heights[right] <= smaller:
                    res += smaller - heights[right]
                    right -= 1
        return res


    def trapRainWater2(self, heights):
        # write your code here
        if not heights:
            return 0
        res = 0
        max_left = [0] * (len(heights) + 1)
        for i in range(len(heights)):
            max_left[i+1] = max(max_left[i], heights[i])

        max_right = 0
        for i in range(len(heights) - 1, -1, -1):
            res += min(max_right, max_left[i]) - heights[i] if min(max_right, max_left[i]) > heights[i] else 0
            max_right = max(max_right, heights[i])
        return res