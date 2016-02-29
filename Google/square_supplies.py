import math
def answer(n):
    # your code here
    limit = int(math.sqrt(n))
    squares = [i**2 for i in range(2, limit+1)]
    print squares
    squares.reverse()
    # res = []
    greed(n, squares)
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
            remain -= squares[j]
            count += 1
        if remain == 0:
            min_len = min(min_len, count)
    return min_len


print answer(14)