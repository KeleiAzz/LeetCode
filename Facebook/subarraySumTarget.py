import sys


def sub_sum(l, target):
    j = 0
    cur_sum = l[0]
    for i in range(1, len(l)):
        while cur_sum > target and j < i - 1:
            cur_sum -= l[j]
            j += 1
        if cur_sum == target:
            print l[j:i]
            return True
        cur_sum += l[i]
    return False


def subMatrixSum(m, target):
    sum_matrix = [m[0]]
    for i in range(1, len(m)):
        sum_matrix.append(map(sum, zip(m[i], sum_matrix[i-1])))
    print sum_matrix
    for i in range(len(m)):
        print sub_sum(sum_matrix[i], target), i, i
        for j in range(i, len(m)):
            row = map(lambda x: x[1] - x[0], zip(sum_matrix[i], sum_matrix[j]))
            print sub_sum(row, target), i, j


if __name__ == "__main__":
    # l = [1, 2, 4, 5, 6,2,3, 4,8, 3,2]
    # t = sys.argv[1]
    # print l
    # print sub_sum(l, int(t))
    mtx = [
        [1,2,3,4],
        [-2,3,5,-1],
        [9,3,-6,2],
        [4,6,-2,9]
    ]
    subMatrixSum(mtx, 5)




