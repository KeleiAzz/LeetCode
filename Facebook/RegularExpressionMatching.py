def isMatch( s, p):
    lenS, lenP = len(s), len(p)
    dp = [[False] * (lenP + 1) for i in range(lenS + 1)]

    # initialization, when p is empty, always Flase, when s is empty:
    dp[0][0] = True
    for j in range(2, lenP + 1):
        dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

    # dp
    for i in range(1, lenS + 1):
        for j in range(1, lenP + 1):
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (p[j - 2] in (s[i - 1], '.') and dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j - 1] and p[j - 1] in ('.', s[i - 1])
    print dp
    return dp[lenS][lenP]

print isMatch('aab', 'c*a*b')



def fibonacci(n):
    p1, p2 = 0, 1
    for i in range(n):
        if i == 0:
            yield 0
        if i == 1:
            yield 1
        p1, p2 = p2, p1 + p2
        yield p2

# f = fibonacci(100)
# for i in range(100):
#     print f.next()