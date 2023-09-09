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
    

        id_hash = {}
        for index in range(len(employees)):
            id_hash[employees[index].id] = employees[index]

        def dfs(node):
            
            total = node.importance
            for subs in node.subordinates:
                total += dfs(id_hash[subs])
            return total
            
        return dfs(id_hash[id])