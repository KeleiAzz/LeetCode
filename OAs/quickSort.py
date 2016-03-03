
def quickSort(nums):
    quickSortHelper(nums, 0, len(nums) - 1)
    return nums


def quickSortHelper(nums, l, r):
    if l < r:
        q = partition(nums, l, r)
        quickSortHelper(nums, l, q - 1)
        quickSortHelper(nums, q + 1, r)


def partition(nums, l, r):
    x = nums[r]
    i = l - 1
    for j in range(l, r):
        if nums[j] <= x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i + 1



t = [23,4,6,23,8,56,34,3,67,8,4,3,12,5,612,3,78]

quickSort(t)
print t