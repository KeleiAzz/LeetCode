class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.matched = []
        if len(board) == 0:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.expand(board, word[1:], i, j, [(i, j)]):
                    return True
        return False


    def expand(self, board, word, i, j, matched):
        if len(word) == 0:
            return True
        if i > 0 and board[i-1][j] == word[0] and (i-1,j) not in matched:
            down = self.expand(board, word[1:], i-1, j, matched+[(i-1,j)])
            if down:
                return True
        if j > 0 and board[i][j-1] == word[0] and (i, j-1) not in matched:
            left = self.expand(board, word[1:], i, j-1, matched+[(i,j-1)])
            if left:
                return True
        if i < len(board)-1 and board[i+1][j] == word[0] and (i+1,j) not in matched:
            up = self.expand(board, word[1:], i+1, j, matched+[(i+1,j)])
            if up:
                return True
        if j < len(board[0]) - 1 and board[i][j+1] == word[0] and (i,j+1) not in matched:
            right = self.expand(board, word[1:], i, j+1, matched+[(i, j+1)])
            if right:
                return True
        return False