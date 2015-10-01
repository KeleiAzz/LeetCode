__author__ = 'keleigong'
class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.l.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.l = self.l[1:]

    def peek(self):
        """
        :rtype: int
        """
        return self.l[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.l) > 0:
            return True
        else:
            return False

q = Queue()

print len(q.l), q.empty()