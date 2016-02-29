class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if '*' not in p and '?' not in p:
            return s == p
        if '*' not in p:
            if len(s) != len(p):
                return False
            else:
                for i in range(len(s)):
                    if s[i] != p[i] and p[i] != '?':
                        return False
                return True
        if len([x for x in p if x != '*']) > len(s):
            return False
        i = 0
        j = 0
        while i < len(s):
            if j == len(p) and p[j-1] == '*':
                return True
            elif j == len(p):
                break
            if s[i] == p[j] or p[j] == '?':
                i += 1
                j += 1
            elif p[j] == '*':

                j += 1
                tmp = ''
                while j < len(p) and p[j] != '*' and p[j] != '?':
                    tmp += p[j]
                    j += 1
                if tmp not in s[i:]:
                    return False
                else:
                    i = i + s[i:].index(tmp) + len(tmp)
            elif s[i] != p[j]:
                return False
        if s[i:] != '':
            print s[i:]
            return False
        return True


s = Solution()

a = "abefcdgiescdfimde"
b = "ab*cd?i*de"
print s.isMatch(a, b)