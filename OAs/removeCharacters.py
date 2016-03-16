def removeCharacters(s, dic):
    c_index = {}
    for i in range(len(s)):
        if s[i] in c_index:
            c_index[s[i]].append(i)
        else:
            c_index[s[i]] = [i]

    index_set = set()
    for word in dic:
        index = getIndex(c_index, word)
        print index
        index_set = index_set | set(index)
    # print index_set
    return len(s) - len(index_set)


def getIndex(c_index, word):
    indeies = [c_index[c] for c in word]
    index_combine = combine(indeies)
    print index_combine
    if len(index_combine) == 1:
        return index_combine[0]
    else:
        return min(index_combine, key=lambda x: x[-1] - x[0])


def combine(indeies):
    if len(indeies) == 1:
        return [[i] for i in indeies[0]]
    res = []
    for i in indeies[0]:
        tmp = combine(indeies[1:])
        for combination in tmp:
            if i < combination[0]:
                res.append([i] + combination)
    # print res
    return res

s = 'applend'
d = ['app', 'len', 'apple', 'end']
print removeCharacters(s, d)