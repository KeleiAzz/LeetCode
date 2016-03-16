class Solution(object):
    def wallsAndGates(self, rooms):
        '''
        BSF with queue
        :param rooms:
        :return:
        '''
        if not rooms:
            return
        m, n = len(rooms), len(rooms[0])
        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] != 0:
                    continue
                queue = [(i, j, 0)]
                while queue:
                    x, y, distance = queue.pop(0)
                    distance += 1
                    for row, col in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                        newX, newY = x + row, y + col
                        if not (0 <= newX < m and 0 <= newY < n) or rooms[newX][newY] in [-1, 0] or distance >= rooms[newX][newY]:
                            continue
                        rooms[newX][newY] = distance
                        queue.append((newX, newY, distance))

    def wallsAndGates2(self, rooms):
        '''
        DFS with a stack
        :param rooms:
        :return:
        '''
        if not rooms:
            return
        m, n = len(rooms), len(rooms[0])
        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] != 0:
                    continue
                stack = [(i, j, 0)]
                while stack:
                    x, y, distance = stack.pop()
                    distance += 1
                    for row, col in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                        newX, newY = x + row, y + col
                        if not (0 <= newX < m and 0 <= newY < n) or rooms[newX][newY] in [-1, 0] or distance >= rooms[newX][newY]:
                            continue
                        rooms[newX][newY] = distance
                        stack.append((newX, newY, distance))


    def wallsAndGates3(self, rooms):
        """
        Recursive way
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if len(rooms) == 0:
            return
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    self.expand(rooms, r, c)

    def expand(self, rooms, r, c):
        if r < 0 or c < 0 or r >= len(rooms) or c >= len(rooms[0]) or rooms[r][c] == -1:
            return
        if rooms[r][c] >= 0:
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if self.isValid(rooms, r+x, c+y) and rooms[r+x][c+y] > rooms[r][c] + 1:
                    rooms[r+x][c+y] = rooms[r][c] + 1
                    self.expand(rooms, r+x, c+y)

    def isValid(self, rooms, r, c):
        if r < 0 or c < 0 or r >= len(rooms) or c >= len(rooms[0]):
            return False
        return True