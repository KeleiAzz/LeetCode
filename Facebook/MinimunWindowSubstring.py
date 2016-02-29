from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        positions = defaultdict(int)
        for l in t:
            positions[l] += 1
        counter = len(t)
        i = 0
        j = 0
        l, r = 0, len(s) - 1
        while j < len(s):
            if s[j] in t:
                positions[s[j]] -= 1
                counter -= 1
            if counter <= 0:
                while i < len(s):
                    if s[i] not in t:
                        i += 1
                    else:
                        if positions[s[i]] + 1 <= 0:
                            positions[s[i]] += 1
                            counter += 1
                            i += 1
                        else:
                            break
                if j - i < r - l and all([x <= 0 for x in positions.values()]):
                    l, r = i, j
            j += 1

        if j == len(s) and any([x > 0 for x in positions.values()]):
            return ""
        return s[l:r+1]


s = Solution()

a = "ADOBECODEBANC"
b = "ABF"

print s.minWindow(a, b)