__author__ = 'keleigong'
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ['(', '[', '{']
        right = [')', ']', '}']
        stack = []
        if s[0] in right:
            return False
        for i in s:
            if i in left:
                stack.append(i)
            if i in right:
                if len(stack) == 0:
                    return False
                if left.index(stack[-1]) == right.index(i):
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True


s = Solution()

print s.isValid("([)]")