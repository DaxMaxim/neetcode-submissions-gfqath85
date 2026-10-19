class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        que, fresh = deque(), 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    que.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        while que and fresh > 0:
            for i in range(len(que)):
                r, c = que.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (0 <= row < ROWS and 0 <= col < COLS and
                        grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh -= 1
                        que.append((row, col))
            minutes += 1
        return -1 if fresh else minutes
                
        