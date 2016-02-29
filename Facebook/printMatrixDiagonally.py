def printMatrix(m):
    if not m:
        return
    i, j = 0, len(m[0]) - 1
    queue = [(i, j)]
    while queue:
        row, col = queue.pop(0)
        print m[row][col]
        if col > 0 and (row, col - 1) not in queue:
            queue.append((row, col - 1))
        if row < len(m) - 1 and (row + 1, col) not in queue:
            queue.append((row + 1, col))

mm = [[1,3,4,51,23],
     [3,5,2,6,2],
     [2,3,5,7,2],
     [4,6,3,5,7]]

printMatrix(mm)

def flatten(nums):
    res = []
    for i in nums:
        if isinstance(i, list):
            res.extend(flatten(i))
        else:
            res.append(i)
    return res


print flatten([1,2,[3,4,[5]]])