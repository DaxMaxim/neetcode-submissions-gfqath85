class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit, q = set(), deque()
        max_area = 0

        def bfs(r, c):
            q.append((r, c))
            visit.add((r, c))
            area = 1

            while q:
                r, c = q.popleft()

                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for dr, dc in directions: 
                    row, col = r + dr, c + dc

                    if (0 <= row < ROWS and 0 <= col < COLS and
                        grid[row][col] == 1 and (row, col) not in visit):
                        q.append((row, col))
                        visit.add((row, col))
                        area += 1
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    max_area = max(max_area, bfs(r, c))
        return max_area
