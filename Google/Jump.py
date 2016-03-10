def JumpArray(arr):
    count = 0
    visited = [0] * len(arr)
    index = 0
    while count < len(arr):
        if visited[index] == 1 and index != 0:
            return False
        elif visited[index] >= 1:
            break
        visited[index] += 1
        index = (index + arr[index]) % len(arr)
        count += 1
    print count
    if index == 0 and count == len(arr):
        return True
    else:
        return False

print JumpArray([1,1,1,1,1,1])
print JumpArray([2,2,3,1])
print JumpArray([7,5,2,3])