class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.lists = vec2d
        self.i = 0
        self.numLists = len(vec2d)

    def next(self):
        """
        :rtype: int
        """
        while self.i < self.numLists and not self.lists[self.i]:
            self.i += 1

        return self.lists[self.i].pop(0) if self.i < self.numLists else None



    def hasNext(self):
        """
        :rtype: bool
        """
        while self.i < self.numLists and not self.lists[self.i]:
            self.i += 1
        return True if self.i < self.numLists else False

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())