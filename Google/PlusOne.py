class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        carry = 1
        for i in range(len(digits)):
            tmp = digits[i] + carry
            digits[i] = tmp if tmp < 10 else tmp - 10
            if tmp < 10:
                carry = 0
                break
            else:
                carry = 1
        if carry == 1:
            digits.append(1)
        return digits[::-1]
