class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        star = -1
        mark = -1
        i, j = 0, 0
        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                star = j
                j += 1
                mark = i
            elif star != -1:
                j = star + 1
                mark += 1
                i = mark
            else:
                return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)