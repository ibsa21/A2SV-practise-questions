#not optimal solution
# time-complexity O(len(s) + len(t))
# space-complexity O( len(s) + len(t))
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for char in s:
            if char == '#':
                if len(stack_s) != 0:
                    stack_s.pop()
            else:
                stack_s.append(char)
        for char in t:
            if char == '#':
                if len(stack_t) != 0:
                    stack_t.pop()
            else:
                stack_t.append(char)
                
        return stack_s==stack_t
