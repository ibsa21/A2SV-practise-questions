class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                temp_stack = []
                while stack[-1] != '(':
                    temp_stack.append(stack.pop())
                stack.pop()
                stack += temp_stack
                     
            else:
                stack.append(char)
            
        return "".join(stack)
                
        
