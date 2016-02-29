class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        num1 = list(reversed(list(num1)))
        num2 = list(reversed(list(num2)))
        res = []
        for i in range(len(num1)):
            tmp = [0] * i + self.Multipy(num2, num1[i])
            res = self.Add(res, tmp)
        res.reverse()
        result = ''.join(map(str, res))
        for i in range(len(result)):
            if result[i] != '0':
                return result[i:]
        return '0'

    def Multipy(self, nums, n):
        n = int(n)
        x = 0
        res = []
        for i in nums:
            tmp = int(n) * int(i) + x
            res.append(tmp % 10)
            x = tmp / 10
        if x:
            res.append(x)
        return res

    def Add(self, num1, num2):
        res = []
        if len(num1) > len(num2):
            num2.extend([0] * (len(num1) - len(num2)))
        else:
            num1.extend([0] * (len(num2) - len(num1)))
        carry = 0
        for i in range(len(num1)):
            tmp = num1[i] + num2[i] + carry
            res.append(tmp % 10)
            carry = tmp / 10
        if carry > 0:
            res.append(carry)
        return res

s =Solution()

s.multiply('123', '11')