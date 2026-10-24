class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def capture(r, c):
            surrounded = True
            que, path = deque(), []

            que.append((r, c))
            visit.add((r, c))
            path.append((r, c))

            while que:
                r, c = que.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if ((row, col) not in visit and 0 < row < ROWS - 1 and 0 < col < COLS - 1 
                        and board[row][col] == "O"):
                        que.append((row, col))
                        visit.add((row, col))
                        path.append((row, col))
                    elif (0 == row or row == ROWS - 1 or 0 == col or col == COLS - 1) and board[row][col] == "O":
                        surrounded = False

            if surrounded:
                for r, c in path:
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visit and 0 < r < ROWS - 1 and 0 < c < COLS - 1:
                    capture(r, c)
 