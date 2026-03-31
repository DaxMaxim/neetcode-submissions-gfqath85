class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        que = deque()
        visit = set()

        def addRoom(r, c):
            if ( r < 0 or r >= rows or
                    c < 0 or c >= cols or
                (r, c) in visit or grid[r][c] == -1):
                return
            visit.add((r, c))
            que.append((r, c))
            

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    que.append((r, c))
                    visit.add((r, c))
        
        dist = 0
        while que:
            for i in range(len(que)):
                r, c = que.popleft()
                grid[r][c] = dist

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1
        

        
