class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        else:
            a = '0' * (len(b) - len(a)) + a
        a = list(reversed(a))
        b = list(reversed(b))
        res = []
        x = '0'
        for i in range(len(a)):
            num_1 = [a[i], b[i], x].count('1')
            if num_1 == 0:
                res.append('0')
                x = '0'
            elif num_1 == 1:
                res.append('1')
                x = '0'
            elif num_1 == 2:
                res.append('0')
                x = '1'
            else:
                res.append('1')
                x = '1'
        if x == '1':
            res.append('1')
        return ''.join(reversed(res))