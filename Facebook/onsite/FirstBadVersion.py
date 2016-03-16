# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binSearch(1, n)

    def binSearch(self, start, end):
        if start >= end:
            if isBadVersion(start):
                return start
            else:
                return start + 1

        mid = (start + end) / 2
        if isBadVersion(mid):
            return self.binSearch(start, mid-1)
        else:
            return self.binSearch(mid+1, end)