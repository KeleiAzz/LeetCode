def fuzzingsub(s):
    res = []
    dfs(s, 0, '', res)
    print res


def dfs(s, start, path, res):
    res.append(path)
    for i in range(start, len(s)):
        dfs(s, i + 1, path+s[i], res)


fuzzingsub('asdfg')