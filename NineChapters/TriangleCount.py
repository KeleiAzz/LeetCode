class Solution:
    # @param S: a list of integers
    # @return: a integer
    def triangleCount(self, S):
        # write your code here
        if len(S) < 3:
            return 0
        S.sort()
        left = 0
        right = len(S) - 1
        count = 0
        while left < right - 1: # For each element from right side, use two sum to count.
            mid = right - 1
            # left = 0
            while left < mid:
                if S[left] + S[mid] > S[right]:
                    count += mid - left
                    mid -= 1
                else:
                    left += 1
            right -= 1
            left = 0
        return count

