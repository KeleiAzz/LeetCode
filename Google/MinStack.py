# from collections import heapq
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.nums:
            self.nums.append((x, min(x, self.nums[-1][1])))
        else:
            self.nums.append((x, x))


    def pop(self):
        """
        :rtype: nothing
        """
        if self.nums:
            self.nums.pop()


    def top(self):
        """
        :rtype: int
        """
        if self.nums:
            return self.nums[-1][0]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.nums:
            return self.nums[-1][1]
        return None

