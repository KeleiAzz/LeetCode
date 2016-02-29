

def solution(split, num_tuples, tuples):
    total_num = sum(map(lambda x: x[1], tuples))
    print total_num
    tuples.sort(key=lambda x: x[0])
    gap = total_num / split
    quantiles = map(lambda x: x * gap, range(1, split))
    num_spent = 0
    q = 0
    t = 0
    res = []
    print quantiles
    while True:
        if q == len(quantiles):
            break

        if quantiles[q] > num_spent:
            num_spent += tuples[t][1]
            t += 1
            continue
        else:
            res.append(tuples[t-1][0])
            q += 1

    return res


print solution(15, 10, [(2, 1), (3, 2), (5, 3), (6, 1), (8, 1), (11, 1), (12, 1), (15, 2), (18, 2), (19, 1)])

