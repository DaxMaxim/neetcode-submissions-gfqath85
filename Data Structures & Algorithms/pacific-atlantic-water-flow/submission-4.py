class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, prev_height, visit):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
                (r, c) in visit or heights[r][c] < prev_height):
                return
            
            visit.add((r, c))

            dfs(r - 1, c, heights[r][c], visit)
            dfs(r + 1, c, heights[r][c], visit)
            dfs(r, c - 1, heights[r][c], visit)
            dfs(r, c + 1, heights[r][c], visit)
   
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, COLS - 1, heights[r][COLS - 1], atlantic)

        for c in range(COLS):
            dfs(0, c, heights[0][c], pacific)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atlantic)

        return list(pacific & atlantic)