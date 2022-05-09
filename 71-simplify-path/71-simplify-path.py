class Solution:
    def simplifyPath(self, path: str) -> str:
        
        path = path.split('/')
        stack_path = []
        
        
        i = 0
        
        print(path)
        while i < len(path):
            
            char  = path[i]
            
            if not char:
                i += 1
                continue
            
            if  '.' in char and len(set(char)) == 1:
                
                len_dot  = len(char)
                if stack_path and  len_dot == 2:
                    stack_path.pop()
                    
                if len_dot > 2:
                    stack_path.append(char)
            else:
                stack_path.append(char)
            i += 1
        
        ans = '/'.join(stack_path)
        return '/' + ans
            
                
            
            
            
            
            