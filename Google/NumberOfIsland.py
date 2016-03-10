def findIsland(matrix):
    res = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                island = []
                expand(matrix, i, j, island)
                res.add(moveIsland(island))
    return len(res)


def expand(matrix, i, j, island):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] != 1:
        return
    island.append([i, j])
    matrix[i][j] = -1
    expand(matrix, i - 1, j - 1, island)
    expand(matrix, i - 1, j, island)
    expand(matrix, i - 1, j + 1, island)
    expand(matrix, i, j - 1, island)
    expand(matrix, i, j + 1, island)
    expand(matrix, i + 1, j - 1, island)
    expand(matrix, i + 1, j, island)
    expand(matrix, i + 1, j + 1, island)


def moveIsland(island):
    min_row = min([x[0] for x in island])
    min_col = min([x[1] for x in island])
    res = ''
    for x, y in island:
        res += str(x-min_row)
        res += '#'
        res += str(y-min_col)
    return res


