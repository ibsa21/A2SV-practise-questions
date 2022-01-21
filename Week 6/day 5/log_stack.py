class Solution:
    def minOperations(self, logs: List[str]) -> int:
        log_stack = []
        for char in logs:
            if char == '../':
                if len(log_stack) != 0:
                    log_stack.pop()
                    
            elif char == './':
                pass
            else:
                log_stack.append(char)
            
        
        return len(log_stack)
