class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        num = "1"
        for i in range(n-1):
            num = self.generate(num)
        return num


    def generate(self, num):
        nums = list(num)
        count = 1
        pre = nums[0]
        res = ''
        for i in range(1, len(nums)):
            if nums[i] == pre:
                count += 1
            else:
                res = res + str(count) + str(pre)
                count = 1
                pre = nums[i]
        res = res + str(count) + str(pre)
        return res
