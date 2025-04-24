class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
      visited = set()
      def dfs(i,j):
        #if exceeded boundary while dfs or not equal to 'O'
        if i<0 or j<0 or j>=len(board[0]) or i>=len(board) or board[i][j] != 'O':
          return
        #mark as visited from the boundary line
        board[i][j] = 'V'
        #dfs the top,right,left and bottom of the cell
        dfs(i-1,j)
        dfs(i,j-1)
        dfs(i+1,j)
        dfs(i,j+1)
      #depth first search of right and left
      for i in range(len(board)):
        dfs(i,0)
        dfs(i,len(board[0])-1)
      #dfs of top and bottom
      for j in range(len(board[0])):
        dfs(0,j)
        dfs(len(board)-1,j)
      for i in range(len(board)):
        for j in range(len(board[0])):
          if board[i][j] == 'V':
            board[i][j] = 'O'
          else:
            board[i][j] = 'X'
        

        
