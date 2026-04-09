class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands, visit = 0, set()

        def bfs(r, c):
            que = deque()
            que.append((r, c))
            visit.add((r, c))

            while que:
                row, col = que.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for  dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (0 <= r < ROWS and 0 <= c < COLS and 
                        grid[r][c] == "1" and (r, c) not in visit):
                        que.append((r, c))
                        visit.add((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == "1": 
                    bfs(r, c)
                    islands += 1
        return islands