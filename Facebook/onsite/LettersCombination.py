from itertools import permutations
from collections import Counter
def subset(word):
    # return list(permutations(word))
    pass
# dfs

print subset('ACRAT')
# def dfs(word, start, )


def searchTrie(root, word):
    res = []
    dfs(root, word, res, '')


def dfs(root, word, res, path):
    if root.val != '/' and (not root or root.val not in word):
        return
    if root.isWord:
        res.append(path+root.val)
    if root.val != '/':
        # tmp.subtract(root. val)
        tmp = word.replace(root.val, '', 1)
        for child in root.children:
            dfs(child, tmp, res, path+root.val)
    else:
        for child in root.children:
            dfs(child, word, res, path)

