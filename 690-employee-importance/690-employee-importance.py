"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        emp_id = {}
        for employee in employees:
            emp_id[employee.id] = employee
            
        
        self.total_importance = 0
        def dfs(employee):
            
            self.total_importance += employee.importance
            
            for emp in employee.subordinates:
                dfs(emp_id[emp])
            
        for employee in employees:
            if employee.id == id:
                dfs(employee)
        
        return self.total_importance
        