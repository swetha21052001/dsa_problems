class Solution:
  def isBipartite(self, graph: List[List[int]]) -> bool:
    self.visited = [False]*len(graph)
    self.colour = [0]*len(graph)
    self.isBipartite = True
    def dfs(node,color):
      if self.visited[node]:
        if self.colour[node]!=color:
          self.isBipartite = False
        return
      self.visited[node] = True
      self.colour[node] = color
      for neigh in graph[node]:
        if color == 1:
          dfs(neigh,2)
        else:
          dfs(neigh,1)
    for i in range(len(graph)):
      if not self.visited[i]:
        dfs(i, 1)
    return self.isBipartite

                
        
