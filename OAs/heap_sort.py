# TODO: implement max heap and min heap


def heapify(nums):
    i = len(nums)/2
    while i >= 0:
        sift(nums, i)
        i -= 1
    # return nums


def sift(nums, k):
    while k < len(nums):
        sm = k
        if k * 2 + 1 < len(nums) and nums[k*2+1] < nums[sm]:
            sm = k * 2 + 1
        if k * 2 + 2 < len(nums) and nums[k*2+2] < nums[sm]:
            sm = k * 2 + 2
        if sm == k:
            break
        nums[k], nums[sm] = nums[sm], nums[k]
        k = sm

def heapSort(nums):
    res = []
    while nums:
        heapify(nums)
        res.append(nums.pop(0))
    return res

t = [23,4,6,23,8,56,34,3,67,8,4,3,12,5,612,3,78]
print heapify(t)
print heapSort(t)