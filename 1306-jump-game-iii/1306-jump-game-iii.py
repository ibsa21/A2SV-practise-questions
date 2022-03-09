class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        length = len(arr)
        q = collections.deque()
        q.append((arr[start], start))
        
        visited = set()
        
        def isValid(i):
            return 0 <= i < length
        
        while q:
            
            value, i = q.popleft()
            
            new_i1 = i + value
            new_i2 = i - value
        
            if (isValid(new_i1) and isValid(new_i2)) and  arr[new_i1]==0 or arr[new_i2]==0:
                return True
            
            if isValid(new_i1) and  new_i1 not in visited:
                visited.add(new_i1)
                q.append((arr[new_i1], new_i1))
            if isValid(new_i2) and  new_i2 not in visited:
                visited.add(new_i2)
                q.append((arr[new_i2], new_i2))
        return False
            
            