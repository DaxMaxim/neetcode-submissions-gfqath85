class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(word_idx, r, c):
            if word_idx == len(word): return True

            if ( r < 0 or c < 0 or 
                 r >= ROWS or c >= COLS or
                 (r, c) in visit or
                board[r][c] != word[word_idx]):
                return False

            visit.add((r, c))
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                if dfs(word_idx + 1, r + dr, c + dc): return True
            visit.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c): return True
        return False