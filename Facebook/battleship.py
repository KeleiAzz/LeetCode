def findAllBattleShip(grid):
    if not grid or len(grid[0]) == 0:
        return 0
    count = 1


def check(grid, i, j):
    nrow = len(grid)
    ncol = len(grid[0])
    if num_occupied(grid, i, j, 'V') == 3:
        if num_occupied(grid, i, j - 1, 'V') > 0 or num_occupied(grid, i, j + 1, 'V') > 0 \
                or (j < ncol - 4 and grid[i][j + 3] == 1) or (j > 0 and grid[i][j - 1] == 1):
            return False
        return True
    if num_occupied(grid, i, j, 'H') == 3:
        if num_occupied(grid, i - 1, j, 'H') > 0 or num_occupied(grid, i + 1, j, 'H') > 0 \
                or (i < nrow - 4 and grid[i + 3][j] == 1) or (i > 0 and grid[i - 1][j] == 1):
            return False
        return True
    return False


def num_occupied(grid, i, j, direction):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return 0
    if direction == 'V':
        occupied = 0
        while i + occupied < len(grid) and grid[i+occupied][j] == 1:
            occupied += 1
        return occupied
    elif direction == 'H':
        occupied = 0
        while j + occupied < len(grid[0]) and grid[i][j+occupied] == 1:
            occupied += 1
        return occupied
    else:
        return 0
