def getMin(keySize, frequency):
    frequency.sort()
    num_press = [1] * len(keySize)
    i = 0
    res = 0
    while frequency:
        f = frequency.pop()
        while keySize[i] == 0:
            if i == len(keySize) - 1:
                i = 0
            else:
                i += 1
        res += f * num_press[i]
        num_press[i] += 1
        keySize[i] -= 1
        if i == len(keySize) - 1:
            i = 0
        else:
            i += 1

    return res


print getMin([3, 1, 2], [3, 3, 3, 2, 1, 1])