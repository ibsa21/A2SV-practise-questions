class Solution:
    def calculate(self, s: str) -> int:
        s= s.replace(" ", "")
        precedence = {'*':2, '/':2, '+':1, '-':1}
        op_stack = []
        result = []
        
        mid_num = ""
        operator_found = 0
        for char in s:
            if char in precedence:
                result.append(mid_num)
                mid_num = ""
                while char in precedence and op_stack and precedence[op_stack[-1]] >= precedence[char]:
                    result += op_stack.pop()

                op_stack.append(char)
            else:
                mid_num += char
        
        result.append(mid_num)
        
        while op_stack:
            result += op_stack.pop()
        
        print(result)
        stack = []
        if len(result) == 1:
            return result[0]
        print(result)
        for char in result:
            print(stack)
            if len(stack) > 1  and char in precedence:
                operator_found += 1
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
            
        return stack[0] if operator_found != 0 else "".join(result)
