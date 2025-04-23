"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
  def getImportance(self, employees: List['Employee'], id: int) -> int:
    graph = defaultdict(list)
    for i in range(len(employees)):
      graph[employees[i].id] = [employees[i].importance, employees[i].subordinates]
    def dfs(node):
      sub = 0
      #print(node[1])
      for neigh in node[1]:
        sub+= dfs(graph[neigh])
      return sub+node[0]
    return dfs(graph[id])
        



        
