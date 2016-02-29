class Solution(object):
    def wallsAndGates(self, rooms):
        """
        Starting from a 0, update and then expand its surroundings
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
            if r > 0 and rooms[r-1][c] != -1 and rooms[r-1][c] > rooms[r][c] + 1:
                rooms[r-1][c] = rooms[r][c] + 1
                self.expand(rooms, r-1, c)
            if c > 0  and rooms[r][c-1] != -1 and rooms[r][c-1] > rooms[r][c] + 1:
                rooms[r][c-1] = rooms[r][c] + 1
                self.expand(rooms, r, c-1)
            if r < len(rooms) - 1 and rooms[r+1][c] != -1 and rooms[r+1][c] > rooms[r][c] + 1:
                rooms[r+1][c] = rooms[r][c] + 1
                self.expand(rooms, r+1, c)
            if c < len(rooms[0]) - 1 and rooms[r][c+1] != -1 and rooms[r][c+1] > rooms[r][c] + 1:
                rooms[r][c+1] = rooms[r][c] + 1
                self.expand(rooms, r, c+1)