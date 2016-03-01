class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        Using list comprehension is much faster than a for loop
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 2:
            return []
        return [''.join([s[:i], '--', s[i+2:]]) for i in xrange(len(s) - 1) if s[i:i+2] == '++']