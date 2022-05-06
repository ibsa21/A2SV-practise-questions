class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        for char in s:
            if stack and char == stack[-1][0]:
                stack[-1][1] +=1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                min_char = [char , 1]
                stack.append(min_char)
        
        string_result = ""
        for array in stack:
            string_result += array[0] * (array[1])
        return string_result
            