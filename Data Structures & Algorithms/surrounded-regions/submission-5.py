class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        unsurrounded = set()

        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                board[r][c] != 'O' or (r, c) in unsurrounded):
                return
            
            unsurrounded.add((r, c))

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)

        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in unsurrounded:
                    board[r][c] = "X"
        

