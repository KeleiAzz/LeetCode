__author__ = 'keleigong'
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        a = list(pattern)
        b = str.split(' ')

        if len(a) != len(b):
            return False
        else:
            a = list(set(a))
            b = list(set(b))
            if len(a) != len(b):
                return False
            project = {}
            for i in range(len(a)):
                project[a[i]] = b[i]
        c = [project[x] for x in a]
        if c == b:
            return True
        return False

s = Solution()

a = "abba"
b = "dog cat cat dog"
print s.wordPattern(a, b)