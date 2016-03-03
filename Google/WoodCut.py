class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0
        start, end = 1, max(L)
        while start + 1 < end:
            mid = start + (end - start) / 2
            if self.count(L, mid) >= k:
                start = mid
            else:
                end = mid
        if self.count(L, end) >= k:
            return end
        if self.count(L, start) >= k:
            return start
        return 0



    def count(self, L, length):
        count = 0
        for i in L:
            count += i / length
        return count