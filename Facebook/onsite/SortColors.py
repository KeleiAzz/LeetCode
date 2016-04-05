def sortColors(nums):
    r, b = 0, len(nums) - 1
    p = 0
    while p <= b:
        if nums[p] == 0:
            nums[p], nums[r] = nums[r], nums[p]
            r += 1
            p += 1
        elif nums[p] == 1:
            p += 1
        else:
            nums[p], nums[b] = nums[b], nums[p]
            b -= 1

def sortColors2(nums):
    '''
    seems difficult to understand
    Just like the Lomuto partition algorithm usually used in quick sort. We keep a loop invariant that
    [0,i) [i, j) [j, k) are 0s, 1s and 2s sorted in place for [0,k). Here ")"
    means exclusive. We don't need to swap because we know the values we want.


    :param nums:
    :return:
    '''
    i = j = 0
    for k in xrange(len(nums)):
        v = nums[k]
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1
        print nums

nums = [1,2,0,0,0,1,1,2,0,1,2,0,1,0,2,1,0]
sortColors2(nums)

def sortKColors(nums, k):
    '''
    if there are k colors, similar approach. idx[i] represents how many numbers are less than i
    :param nums:
    :param k:
    :return:
    '''
    idx = [0] * k
    for i in xrange(len(nums)):
        v = nums[i]
        nums[i] = k - 1
        for j in range(1, k)[::-1]:
            if v < j:
                nums[idx[j-1]] = j - 1
                idx[j-1] += 1
    return nums

nums2 = [1,3,4,2,3,1,2,3,0,3,1,0,4,3,2,1,0,0,2,4,3,1]
print sortKColors(nums2, 5)

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    prepre, pre = 1, 1
    for i in range(3, n+1):
        prepre, pre = pre, prepre + pre
        print pre
    return pre


# fibonacci(60)