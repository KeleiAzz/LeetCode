def partition(nums, l, r):
    x = nums[r]
    i = l - 1
    for j in range(l, r):
        if nums[j] <= x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i + 1

def partition2(nums, l, r):
    if l == r:
        return l
    left, right = l, r
    now = nums[left]
    while left < right:
        while left < right and nums[right] >= now:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= now:
            left += 1
        nums[right] = nums[left]
    nums[left] = now
    return left


def select(nums, l, r, n):
    if l == r:
        return nums[l]
    pivotIndex = partition2(nums, l, r)
    if n == pivotIndex:
        return nums[n]
    elif n < pivotIndex:
        return select(nums, l, pivotIndex - 1, n)
    else:
        return select(nums, pivotIndex + 1, r, n)


import random

def generate(n):
    res = []
    for _ in xrange(n):
        res.append(random.randint(0, n))
    return res

for i in range(100):
    nums = generate(200)
    k = random.randint(0, 199)
    # print nums
    true = sorted(nums)[k]
    predict = select(nums, 0, 199, k)
    assert true == predict, '%d != %d' % (true, predict,)

    # assert  ==
