def shortestPath(matrix, p1, p2):
    if not matrix:
        return -1
    queue = [(p1[0], p1[1], 0)]
    m, n = len(matrix), len(matrix[0])
    path = []
    visited = set()
    while queue:
        x, y, dist = queue.pop(0)
        while path and path[-1][2] >= dist:
            path.pop()
        path.append((x, y, dist))
        dist += 1
        for row, col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            newX, newY = x + row, y + col
            if newX < 0 or newY < 0 or newX >= m or newY >= n or matrix[newX][newY] == 1 or (newX, newY) in visited:
                continue
            if newX == p2[0] and newY == p2[1]:
                print path
                return dist
            queue.append((newX, newY, dist))
            visited.add((newX, newY))


m = [
    [0,0,1,0,0,0],
    [0,1,0,0,1,1],
    [0,1,0,0,0,0],
    [0,0,1,1,1,0],
    [0,0,0,0,0,0]
]

print shortestPath(m, (0, 0), (0, 5))