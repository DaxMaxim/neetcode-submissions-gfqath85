class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()

        def bfs(r, c, visit):
            q.append((r, c))
            visit.add((r, c))

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    
                    if (0 <= row < ROWS and 0 <= col < COLS and 
                        (row, col) not in visit and heights[row][col] >= heights[r][c]):
                        q.append((row, col))
                        visit.add((row, col))
        
        for c in range(COLS):
            # for pacific
            if (0, c) not in pacific:
                bfs(0, c, pacific)
            # for atlantic
            if (ROWS - 1, c) not in atlantic:
                bfs(ROWS - 1, c, atlantic)
        
        for r in range(ROWS):
            # for pacific
            if (r, 0) not in pacific:
                bfs(r, 0, pacific)
            # for atlantic
            if (r, COLS - 1) not in atlantic:
                bfs(r, COLS - 1, atlantic)

        result = [list(t) for t in pacific & atlantic]
        return result