class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands, visit = 0, set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # def bfs(r, c):
        #     que = deque()

        #     que.append((r, c))
        #     visit.add((r, c))

        #     while que:
        #         r, c = que.popleft()

        #         for dr, dc in directions:
        #             row, col = r + dr, c + dc

        #             if (0 <= row < ROWS and 0 <= col < COLS
        #                 and grid[row][col] == "1" and (row, col) not in visit):
        #                 que.append((row, col))
        #                 visit.add((row, col))

        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                grid[r][c] != "1" or (r, c) in visit):
                return
            
            visit.add((r, c))

            for dr, dc in directions:
                row, col = r + dr, c + dc
                dfs(row, col)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    # bfs(r, c)
                    dfs(r, c)
                    islands += 1
        return islands