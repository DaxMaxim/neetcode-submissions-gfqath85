class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        que = deque()

        def addRoom(r, c):
            # if the room is valid add it to the que else do nothing
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == -1 or
                (r, c) in visit):
                return
            que.append((r, c))
            visit.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    que.append((r, c))
                    visit.add((r, c))
        
        dist = 0
        while que:
            for i in range(len(que)):
                r, c = que.popleft()

                # update the distance, go 4 directions
                grid[r][c] = dist

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            # increase the distance
            dist += 1

        

        
