class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        q = deque()
        def addBlock(r,c,grid):
            if (r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == -1 or (r,c)  in visited):
                return
            visited.add((r,c))
            q.append([r,c])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append([r,c])
        distance = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = distance

                addBlock(r+1,c,grid)
                addBlock(r-1, c, grid)
                addBlock(r,c+1, grid)
                addBlock(r,c-1, grid)
            distance +=1 

            


        