class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      #create a visited set
      visited = set()
      def dfs(i,j):
        #Edge cases were the grid becomes 0-> water or reached the end of the graph return       
      	if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0 or grid[i][j] == '0':
            return
        #if the node was already visited return
        if (i,j) in visited:
          return
        # Add the indices to the visited set
        visited.add((i,j))
        #parse in above, below, left and right depth wise
        dfs(i,j+1)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i-1,j)
        return
      count = 0
      for i in range(len(grid)):
        for j in range(len(grid[0])):
          #dfs for the node(indices) which was not visited
          if grid[i][j] == "1" and (i,j) not in visited:
            dfs(i,j)
            count+=1
      return count
