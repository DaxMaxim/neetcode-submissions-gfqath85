class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh, minutes = 0, 0
        que = deque()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    que.append((r, c))

        while que and fresh > 0:

            for i in range(len(que)):
                r, c = que.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (row < 0 or row >= ROWS or col < 0 or col >= COLS or
                        grid[row][col] != 1):
                        continue
                    que.append((row, col))
                    grid[row][col] = 2
                    fresh -= 1
            minutes += 1

        return -1 if fresh else minutes