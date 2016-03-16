class Solution(object):
    def numDecodings(self, s):
        '''
        DP with space o(n)
        :param s:
        :return:
        '''
        if len(s) == 0 or int(s[0]) == 0:
            return 0
        count = [1 for i in xrange(len(s)+1)]
        for i in xrange(2, len(s)+1):
            count[i] = count[i-1]
            if int(s[i-2]) > 0 and int(s[i-2]+s[i-1]) <= 26:
                count[i] = count[i-2] + (count[i-1] if int(s[i-1]) > 0 else 0) # if curr char is zero, don't add prev count
            if int(s[i-1]) == 0 and not (1 <= int(s[i-2]+s[i-1]) <= 26): # if encounter invalid sequence, terminate early
                return 0
        return count[len(s)]

    def numDecodings2(self, s):
        """
        DP with space o(1)
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        pre, cur = 1, 1
        for i in range(1, len(s)):
            if s[i] == '0':
                cur = 0
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                pre, cur = cur, cur + pre
            else:
                pre = cur
        return cur

    def numDecodings3(self, s):
        """
        Recursive with memorization.
        :type s: str
        :rtype: int
        """
        if (s == ""):
            return 0
        return self.decodingHelper(s, {})

    def decodingHelper(self, s, memoDict):
        if len(s) == 0:
            return 1
        if s[0] == "0":
            return 0
        if not s in memoDict:
            numWays = 0
            if len(s) >= 2 and int(s[0:2]) <= 26:
                numWays += self.decodingHelper(s[2:], memoDict)
            numWays += self.decodingHelper(s[1:], memoDict)
            memoDict[s] = numWays
        return memoDict[s]