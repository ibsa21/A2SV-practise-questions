class Solution:
    def decodeString(self, s: str) -> str:

        frequency_stack = []
        string_stack = []

        idx = 0

        while idx < len(s):
            
            char = s[idx]
            while char.isdigit() and  idx+1 < len(s) and s[idx+1].isdigit():
                char += s[idx+1]
                idx += 1

            if char.isdigit():
                frequency_stack.append(int(char))
            elif char == ']':
                frequency = frequency_stack.pop()
                current_string = deque()

                while string_stack and  string_stack[-1] != '[':
                    current_string.appendleft(string_stack.pop())   

                string_stack.pop()
                string_stack.append((''.join(current_string))*frequency)
            else:
                string_stack.append(char) 
            
            idx += 1
                    
        return ''.join(string_stack)