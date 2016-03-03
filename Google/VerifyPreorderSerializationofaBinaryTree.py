class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        s = preorder.split(',')
        n = s.count('#')
        if n != len(s) - n + 1:
            return False
        # return True
        i = len(s) - 1
        while i >= 0:
            if s[i] != '#':
                if not s or s.pop() != '#':
                    return False
                if not s or s.pop() != '#':
                    return False
                s[i] = '#'
            i -= 1
        return len(s) == 1 and s[0] == '#'