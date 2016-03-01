import math

def answer(n):
    '''
    Actually this approach does NOT work...
    '''
    # your code here
    limit = int(math.sqrt(n))
    squares = [i**2 for i in range(1, limit+1)]
    print squares
    squares.reverse()
    # res = []
    return greed(n, squares)
    # print res


def greed(n, squares):
    min_len = float('INF')
    for i in range(len(squares)):
        remain = n - squares[i]
        count = 1
        while count < min_len and remain > 0:
            j = 0
            while j < len(squares) and squares[j] > remain:
                j += 1
            print remain, squares[j],
            remain -= squares[j]

            count += 1
        if remain == 0:
            min_len = min(min_len, count)
        print ' '
    return min_len


def perfectSquares(n):
    '''
    A DP way to solve this, but still seems to slow
    :param n:
    :return:
    '''
    dp = [float('INF')] * (n + 1)
    for i in xrange(1, n+1):
        sqt = int(math.sqrt(i))
        if sqt * sqt == i:
            dp[i] = 1
        else:
            dp[i] = 1 + min([dp[i-j*j] for j in range(1, sqt+1)])
    return dp[-1]

cache ={}
def numSquares(n):
    '''
    Using a cache, quick but seems not work when n get large
    :param n:
    :return:
    '''
    global cache
    if n == 0:
        return 0
    if n < 0:
        return float('INF')
    if n in cache:
        return cache[n]
    else:
        ans = 1 + min([numSquares(n - i * i) for i in range(1, int(math.sqrt(n)) + 1)])
        cache[n] = ans
    return cache[n]
# print answer(48)


print numSquares(2031)