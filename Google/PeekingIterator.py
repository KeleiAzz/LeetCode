# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.buff = self.iterator.next()
        self.end = 0

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.buff


    def next(self):
        """
        :rtype: int
        """
        # tmp = self.buff
        # self.buff = self.iterator.next()
        if self.iterator.hasNext():
            tmp = self.buff
            self.buff = self.iterator.next()
            # self.end = 0
            return tmp
        elif not self.iterator.hasNext() and not self.end:
            self.end = 1
            return self.buff
        else:
            return None



    def hasNext(self):
        """
        :rtype: bool
        """
        if self.iterator.hasNext():
            return True
        elif not self.end:
            return True
        else:
            return False



# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].