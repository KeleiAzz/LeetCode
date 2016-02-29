class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        if ' ' not in s:
            return
        s.reverse()
        i = 0
        for j in range(len(s)):
            if s[j].isspace():
                s[i:j] = s[i:j][::-1]
                i = j + 1
        s[i:] = s[i:][::-1]