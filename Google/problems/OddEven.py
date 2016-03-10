def rmEvenDupOdd(nums):
    odd_buffer = []
    i = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            if odd_buffer:
                nums[i] = odd_buffer.pop()
                i += 1
            else:
                nums[i].pop(i)
        else:
            odd_buffer.append(nums[i])
            i += 1
    if odd_buffer:
        nums.extend(odd_buffer)
    return nums


n = [1,3,5,7,4,4,6,7,3,4,6]

print rmEvenDupOdd(n)