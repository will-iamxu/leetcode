class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or c >= col or r >= row or word[i] != board[r][c] or board[r][c] == "#"):
                return False
            board[r][c] = "#"
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            board[r][c] = word[i]
            return res
        
        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        return False 
            