import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        Using two heaps to maintain first half and second half numbers
        """
        self.small = []
        self.large = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        heap push and heap pop can be done in logn
        If using a list, may need o(n) time
        :type num: int
        :rtype: void
        """
        if not self.small:
            self.small.append(-num)
            return
        if num <= - self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        if len(self.small) - len(self.large) == 2:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) - len(self.small) == 2:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        else:
            mid = -self.small[0] if len(self.small) > len(self.large) else self.large[0]
            return mid

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()