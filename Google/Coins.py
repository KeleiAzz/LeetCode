cache = {}

def sumToK(k):
    global cache
    coins = [1, 2, 5, 10]
    if k in coins:
        return 1
    if k < 0:
        return float('INF')
    if k in cache:
        return cache[k]
    else:
        ans = 1 + min([sumToK(k - i) for i in coins])
        cache[k] = ans
    return cache[k]

print sumToK(121)
