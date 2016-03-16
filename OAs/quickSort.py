
def quickSort(nums):
    quickSortHelper(nums, 0, len(nums) - 1)
    return nums


def quickSortHelper(nums, l, r):
    if l < r:
        q = partition(nums, l, r)
        quickSortHelper(nums, l, q - 1)
        quickSortHelper(nums, q + 1, r)


def partition(nums, l, r):
    '''
    Lomuto-Partition. Positions before i and in i is less than pivot, positions after i before j are greater than pivot
    :param nums:
    :param l:
    :param r:
    :return:
    '''
    x = nums[r]
    i = l - 1
    for j in range(l, r):
        if nums[j] <= x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i + 1

def partition2(nums, l, r):
    x = nums[l]
    i = l
    j = r
    while True:
        while nums[j] > x:
            j -= 1
        while nums[i] < x:
            i += 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            return j

t = [23,4,6,23,8,56,34,3,67,8,4,3,12,5,612,3,78]

quickSort(t)
print t