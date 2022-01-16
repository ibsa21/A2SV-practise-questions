class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for char in s:
            stack.append(char)
            if (len(stack) >= len(part) and char == part[-1]):
                string = str()
                for i in range(len(stack)-1, len(stack)-(len(part) + 1), -1):
                    string += stack[i]
                    
                if string[::-1] == part:
                    stack = stack[:-(len(part))]
        return "".join(stack)
