class Solution:
  def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
      graph = defaultdict(list)
      visited = [0]*n
      self.maxTime = 0
      for i in range(len(manager)):
        if headID != i:
          graph[manager[i]].append(i)
      print(graph)
      queue = []
      def dfs(node):
        if node not in graph:
          return 0
        visited[node] = 1
        final_visit = 0
        for neigh in graph[node]:
          final_visit = max(final_visit, dfs(neigh))
        return final_visit+informTime[node]
      return dfs(headID)

        
