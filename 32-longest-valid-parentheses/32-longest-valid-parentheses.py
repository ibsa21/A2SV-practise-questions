class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = [-1]
        
        longest = 0
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            else:
                stack.pop()
                if len(stack) > 0:
                    longest = max(longest, (index-stack[-1]))
                else:
                    stack.append(index)             
        return longest
        