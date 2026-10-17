class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        que = deque()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    que.append((r, c))
        
        level = 1
        while que:

            for i in range(len(que)):
                r, c = que.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (0 <= row < ROWS and 0 <= col < COLS 
                        and grid[row][col] == 2147483647):
                        que.append((row, col))
                        grid[row][col] = level
            level += 1

