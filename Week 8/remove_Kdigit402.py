class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        mono_stack = []
        
        for i in range(len(num)):
            num_x = num[i]
            while mono_stack and int(num_x) < int(mono_stack[-1]) and k > 0:
                mono_stack.pop()
                k -= 1
            
            mono_stack.append(num_x)
        
        while k:
            mono_stack.pop()
            k -= 1
        
        result = "".join(mono_stack)
        
        if  not mono_stack:
            return "0"
        else:
            return str(int(result))
                
        
