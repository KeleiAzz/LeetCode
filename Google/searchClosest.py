def searchClosest(arr, num):
    left, right = 0, len(arr) - 1
    # if num < arr[0]:
    #     return 0
    # elif num > arr[-1]:
    #     return len(arr) - 1
    while left < right:
        mid = (left + right) / 2
        if arr[mid] <= num <= arr[mid+1]:
            return mid if abs(arr[mid] - num) < abs(arr[mid+1]-num) else mid+1
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid


arr = [1,3,5,7,8,10,12]
num = 11.1

print searchClosest(arr, num)