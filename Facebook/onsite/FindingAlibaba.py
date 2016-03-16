def alibaba(numCaves, strategy):
    days = len(strategy)
    res = [[False] * days for _ in xrange(numCaves)]
    for i in range(days):
        res[strategy[i]][i] = True

    for i in range(numCaves):
        for j in range(1, days):
            if i == numCaves - 1:
                res[i][j] = res[i][j] or res[i-1][j-1]
            elif i == 0:
                res[i][j] = res[i][j] or res[i+1][j-1]
            else:
                res[i][j] = res[i][j] or (res[i-1][j-1] and res[i+1][j-1])

    result = True
    for i in range(numCaves):
        if not result:
            break
        else:
            result = result and res[i][days-1]

    return result

strategy = [0,3,1,4,4,3,2,3,1,4,3,4,4,3,1]




def canFind(numCaves, strategy):
    def helper(pos, curr):
        if curr == len(strategy):
            return False
        if pos == strategy[curr]:
            return True
        res = True
        if pos > 0:
            res = res and helper(pos - 1, curr + 1)
        if pos < numCaves - 1:
            res = res and helper(pos + 1, curr + 1)
        return res
    for i in xrange(numCaves):
        if helper(i, 0) is False:
            return False
    return True


print canFind(5, strategy)