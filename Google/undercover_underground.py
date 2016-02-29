from itertools import combinations
from math import factorial
def answer(N, K):
    all_edges = list(combinations(range(N), 2))
    testset = combinations(all_edges, K)
    count = 0
    for test in testset:
        tmp = set()
        for edge in test:
            tmp.add(edge[0])
            tmp.add(edge[1])
        if len(tmp) == N:
            count += 1
            # print test
    return count



print answer(4, 3), answer(4, 4), answer(4, 5), answer(4, 6)
print answer(5, 4), answer(5, 5), answer(5, 6), answer(5, 7), answer(5, 8), answer(5, 9), answer(5, 10)
print answer(6, 5), answer(6, 6), answer(6, 7), answer(6, 8), answer(6, 9), answer(6, 10), answer(6, 11)
print answer(7, 6)

def answer2(N, K):
    count = 0
    for i in range(N+1):
        ci = combine(i, 2)
        count += (-1) ** (N-i) * combine(N, i) * combine(ci, K)
    return count


def combine(n, k):
    if k > n:
        return 0
    return factorial(n) /(factorial(k) * factorial(n-k))

print answer2(5, 4), answer2(5, 5), answer2(5, 6), answer2(5, 7), answer2(5, 8), answer2(5, 9), answer2(5, 10)
print answer2(6, 5), answer2(6, 6), answer2(6, 7), answer2(6, 8), answer2(6, 9), answer2(6, 10), answer2(6, 11)
print answer2(14, 20)

def answer3(N, K):
    if K == N * (N - 1) / 2:
        return 1
    if K < N - 1 or K > N * (N - 1) / 2:
        return 0
    base = combine(combine(N, 2), K)
    i = 1
    while i < N:
        tmp = answer3(N - i, K)
        if tmp > 0:
            base -= combine(N, i) * tmp
            i += 1
        else:
            break
    return base

print answer3(5, 4), answer3(5, 5), answer3(5, 6), answer3(5, 7), answer3(5, 8), answer3(5, 9), answer3(5, 10)
print answer3(7, 10)