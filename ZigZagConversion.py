__author__ = 'keleigong'
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # row = []
        rows = []
        for i in range(numRows):
            rows.append([])
        res = ''
        row_num = -1
        nums = []
        direction = 1
        i = 0
        while i < len(s):
            row_num += direction * 1
            nums.append(row_num)
            if row_num == 0:
                direction = 1
            elif row_num == numRows - 1:
                direction = -1
            i += 1
        print nums
        for i in range(len(s)):
            rows[nums[i]].append(s[i])
        print rows
        for i in range(numRows):
            res += ''.join(rows[i])
        return res


s = Solution()
k = "PAYPALISHIRINGPAYPALISHIRING"

print s.convert(k, 5)