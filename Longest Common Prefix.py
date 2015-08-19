__author__ = 'keleigong'


class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        res = ''
        j = 0
        if strs:
            while(j < len(strs[0])):
                l = strs[0][j]
                for i in strs:
                    if j >= len(i) or i[j] != l:
                        return res
                res += l
                j += 1
            return res
        else:
            return ''

s = Solution()

k = ['aa', 'a']
print s.longestCommonPrefix(k)