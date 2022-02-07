class Solution:
    def decodeString(self, s: str) -> str:
        """
            Complexity analysis
            Time complexity O(n)
            Space complexity O(n)
        """
        stack_no = []
        stack = []
        
        counter = 0 
        
        while counter < len(s):
            char = s[counter]
            
            if  char == ']':
                min_result = [] 
                while stack and  stack[-1] != '[':
                    min_result.append(stack.pop())
                    
                stack.pop()
                stack.append("".join(min_result[::-1]) *stack_no.pop())
                
            elif char.isnumeric():
                num = ''
                while s[counter].isnumeric():
                    num += s[counter]
                    counter += 1
                if num != '':
                    stack_no.append(int(num))
                counter -=1
            else:
                stack.append(char)
                
            counter += 1
                
        return "".join(stack)
    
