class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 3:
            return len(s)
        p1, p2 = 0, 2
        max_length = 2
        c = set()
        # start_from =
        while p1 < len(s) - 1:
            start_from = p1 + 1
            c.add(s[p1])
            c.add(s[p1+1])
            p2 = p1 + 2
            while p2 < len(s) + 1:
                if p2 == len(s):
                    max_length = max(max_length, p2 - p1)
                    break
                c.add(s[p2])
                if len(c) > 2:
                    max_length = max(max_length, p2 - p1)
                    break
                else:
                    if s[p2] != s[p2-1]:
                        start_from = p2
                    p2 += 1

            p1 = start_from
            c = set()
        return max_length