def powerSet(nums):
    res = []
    i = 0
    while i < 2**len(nums):
        sub = bin(i)[2:]
        sub = '0' * (len(nums) - len(sub)) + sub
        print sub
        tmp = []
        for c in range(len(sub)):
            if sub[c] == '1':
                tmp.append(nums[c])
        res.append(tmp)
        i += 1
    return res

def powerSet2(nums):
    res = []
    dfs(sorted(nums), 0, [], res)
    return res

def dfs(nums, start, path, res):
    res.append(path)
    for i in range(start, len(nums)):
        dfs(nums, i+1, path+[nums[i]], res)


a = [1, 2, 3]
print powerSet(a)
print powerSet2(a)
