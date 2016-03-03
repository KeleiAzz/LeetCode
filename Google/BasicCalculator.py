class Solution(object):
    def calculate(self, s):
        """
        A better solution
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        num, res, sign, stack = 0, 0, 1, [1]
        for i in s + '+':
            if i.isdigit():
                num = num * 10 + int(i)
            elif i in '+-':
                res += num * sign * stack[-1]
                sign = -1 if i == '-' else 1
                num = 0
            elif i == '(':
                stack.append(sign * stack[-1])
                sign = 1
            elif i == ')':
                res += num * sign * stack[-1]
                num = 0
                stack.pop()
        return res


    def calculate2(self, s):
        """
        Not a good solution
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if '(' not in s and ')' not in s:
            print s
            tmp = s.split('+')
            to_sum = []
            for sub in tmp:
                sub.strip()
                if '-' in sub:
                    if sub[0] != '-':
                        tmp2 = sub.split('-')
                        res = int(tmp2[0])
                    else:
                        tmp2 = sub[1:].split('-')
                        res = -int(tmp2[0])
                    for i in range(1,len(tmp2)):
                        res -= int(tmp2[i])
                    to_sum.append(res)
                else:
                    to_sum.append(int(sub))
            return sum(to_sum)
        else:
            print s
            stack = []
            for c in s:
                if c != ')':
                    stack.append(c)
                else:
                    sub = ''
                    while stack[-1] != '(':
                        sub = stack.pop() + sub
                    sub_res = self.calculate(sub)
                    stack.pop()
                    if sub_res >= 0:
                        stack.append(str(sub_res))
                    else:
                        stack[-1] = '-' if stack[-1] == '+' else '+'
                        stack.append(str(-sub_res))
            return self.calculate(''.join(stack))


s = Solution()
print s.calculate("(5-(1+(5)))")