class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = {'+', '-', '*', '/', '%'}
        if len(tokens) == 1:
            return tokens[0]
        for char in tokens:
            if len(stack) > 1  and char in operation:
                num2 = stack.pop()
                num1 = stack.pop()
                if char == '+':
                    stack.append(num1 + num2)
                elif char == '-':
                    stack.append(num1-num2)
                elif char == '*':
                    stack.append(num1 * num2)
                elif char == '/':
                    stack.append(math.trunc(num1/num2))
            else:
                stack.append(int(char))
            
        return stack[0]
                    
