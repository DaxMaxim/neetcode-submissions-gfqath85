class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(word_idx, r, c):
            visit.add((r, c))
            if word_idx >= len(word)-1 : return True
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                if (0 <= r + dr < ROWS and 
                    0 <= c + dc < COLS and 
                    word_idx + 1 < len(word) and (r + dr, c + dc) not in visit and
                    board[r + dr][c + dc] == word[word_idx + 1]):
                    if dfs(word_idx + 1, r + dr, c + dc):
                        # visit.remove((r, c))
                        return True
            visit.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(0, r, c): 
                    return True
        return False