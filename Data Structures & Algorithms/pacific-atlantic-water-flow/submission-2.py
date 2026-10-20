class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, prev_height, visit): # out of bounds, coordinate in visit set, or is smaller, return
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
                (r, c) in visit or heights[r][c] < prev_height):
                return
            
            # add the element in the visit set
            visit.add((r, c))

            dfs(r - 1, c, heights[r][c], visit)
            dfs(r + 1, c, heights[r][c], visit)
            dfs(r, c - 1, heights[r][c], visit)
            dfs(r, c + 1, heights[r][c], visit)
   
        for r in range(ROWS):
            if (r, 0) not in pacific:
                dfs(r, 0, heights[r][0], pacific)
            if (r, COLS - 1) not in atlantic:
                dfs(r, COLS - 1, heights[r][COLS - 1], atlantic)

        for c in range(COLS):
            if (0, c) not in pacific:
                dfs(0, c, heights[0][c], pacific)
            if (ROWS - 1, c) not in atlantic:
                dfs(ROWS - 1, c, heights[ROWS - 1][c], atlantic)

        return list(pacific & atlantic)