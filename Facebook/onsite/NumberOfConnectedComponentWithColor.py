def countComponents(matrix):
    count = {}
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]:
                if matrix[i][j] in count:
                    count[matrix[i][j]] += 1
                    dfs(matrix, i, j, matrix[i][j])
                else:
                    count[matrix[i][j]] = 1
                    dfs(matrix, i, j, matrix[i][j])
    print count
    # print matrix

def dfs(matrix, i, j, color):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] != color:
        return
    matrix[i][j] = 0
    dfs(matrix, i - 1, j, color)
    dfs(matrix, i + 1, j, color)
    dfs(matrix, i, j - 1, color)
    dfs(matrix, i, j + 1, color)


m = [
    ['r', 'r', 'r', 'b', 'b', 'g'],
    ['r', 'r', 'b', 'b', 'g', 'g'],
    ['g', 'g', 'b', 'r', 'r', 'g'],
    ['r', 'g', 'g', 'b', 'r', 'r'],
    ['r', 'b', 'g', 'b', 'b', 'r'],
    ['b', 'b', 'r', 'r', 'g', 'g']
]

countComponents(m)