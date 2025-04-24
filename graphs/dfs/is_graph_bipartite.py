class Solution:
  def isBipartite(self, graph: List[List[int]]) -> bool:
    self.visited = [False]*len(graph)
    self.colour = [0]*len(graph)
    self.isBipartite = True
    def dfs(node,color):
      if self.visited[node]:
        #if a node is already visited and already coloured with a different color, the graph is not a bipartite
        if self.colour[node]!=color:
          self.isBipartite = False
        return
      self.visited[node] = True
      self.colour[node] = color
      #if the color of parent is one, color the neighbor with 2 and vice versa
      for neigh in graph[node]:
        if color == 1:
          dfs(neigh,2)
        else:
          dfs(neigh,1)
    #parse all unvisited nodes
    for i in range(len(graph)):
      if not self.visited[i]:
        dfs(i, 1)
    return self.isBipartite

                
        
