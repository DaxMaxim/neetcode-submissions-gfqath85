class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0: q.append((r, c))

        level = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        while q:
            level += 1

            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (0 <= row < ROWS and 0 <= col < COLS and
                        grid[row][col] == 2147483647):
                        grid[row][col] = level
                        q.append((row, col))
            