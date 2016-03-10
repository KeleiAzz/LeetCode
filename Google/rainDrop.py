import random
def sample(n):
    d = dict(zip(range(n), [1] * n))
    count = 0
    while d:
        count += 1
        tmp = random.randrange(0, n, 1)
        if tmp in d:
            d.pop(tmp)

    return count

total = 0
for i in range(1000):
    total += sample(100)


print total / 1000