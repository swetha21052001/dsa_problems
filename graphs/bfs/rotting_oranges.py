class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        fresh_oranges = 0
        vector = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh_oranges+=1
        minutes_elapsed = 0
        while queue:
            r,c,minutes_elapsed = queue.pop(0)
            for dr,dc in vector:
                nr = r+ dc
                nc = c+ dr
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc]=2
                    fresh_oranges -=1
                    queue.append((nr,nc,minutes_elapsed+1))
        return minutes_elapsed if fresh_oranges==0 else -1
