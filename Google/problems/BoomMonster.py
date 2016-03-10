def boomMonster(matrix):
    dp_h = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    # dp_v = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        count = 0
        j, k = 0, 0
        while j < n and k < n:
            if matrix[i][k] == 0:
                k += 1
            elif matrix[i][k] == 1:
                count += 1
                k += 1
            else:
                dp_h[i][j:k] = [count] * (k - j)
                count = 0
                k += 1
                j = k
        dp_h[i][j:k] = [count] * (k - j)
    print dp_h

    max_count = 0
    for i in range(n):
        count = 0
        j, k = 0, 0
        while j < m and k < m:
            if matrix[k][i] == 0:
                k += 1
            elif matrix[k][i] == 1:
                count += 1
                k += 1
            else:
                for p in range(j, k):
                    # dp_v[p][i] = count + dp_h[p][i]
                    max_count = max(max_count, count + dp_h[p][i])
                count = 0
                k += 1
                j = k
        for p in range(j, k):
            # dp_v[p][i] = count + dp_h[p][i]
            max_count = max(max_count, count + dp_h[p][i])
    # print dp_v
    return max_count



m  = [[0,0,1,1,-1,0,0,1,-1],
      [1,0,1,-1,0,1,1,0,-1],
      [1,1,0,0,-1,0,-1,0,1],
      [0,1,-1,0,1,0,1,1,-1]]

print boomMonster(m)