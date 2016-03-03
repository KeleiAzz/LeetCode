class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        # states = [[0] * len(board[0]) for _ in range(len(board))]
        states = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                live = self.liveNeighbors(board, i, j)
                if board[i][j] and live < 2:
                    states.append((i, j))
                elif board[i][j] and live > 3:
                    states.append((i, j))
                elif not board[i][j] and live == 3:
                    states.append((i, j))
        for i, j in states:
            board[i][j] = 0 if board[i][j] else 1


    def liveNeighbors(self, board, i, j):
        neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        count = 0
        for p, q in neighbors:
            if self.live(board, i+p, j+q):
                count += 1
        return count

    def live(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return False
        return True if board[i][j] else False