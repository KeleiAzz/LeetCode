__author__ = 'keleigong'
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
        i = 0
        j = len(s) - 1
        s = s.lower()
        while i <= j:
            print i, j
            if s[i] not in letters:
                i += 1
                continue
            if s[j] not in letters:
                j -= 1
                continue
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

s = Solution()

ss = "1a2"
print s.isPalindrome(ss)