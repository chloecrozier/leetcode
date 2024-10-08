# https://leetcode.com/problems/word-search/description/
class Solution:
    def search(self, board, r, c, word):
        found = False
        if len(word) == 0:
            return True
        if r >= len(board) or r < 0 or c >= len(board[0]) or c < 0:
            return False

        if board[r][c] != word[0]:
            return False

        temp = board[r][c]
        board[r][c] = None
        found = (self.search(board, r + 1, c, word[1:]) or
                self.search(board, r - 1, c, word[1:]) or
                self.search(board, r, c + 1, word[1:]) or
                self.search(board, r, c - 1, word[1:]))
        board[r][c] = temp
        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    print(r, c)
                    if self.search(board, r, c, word):
                        return True
        return False
