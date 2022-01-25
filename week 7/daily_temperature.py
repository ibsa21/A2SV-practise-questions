class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

    
        result1 = [0] * len(temperatures)
        stack1 = []
        # stack [7, 6, ]
        for i in range(len(temperatures)-1, -1, -1):
            while stack1 and temperatures[i] < temperatures[stack1[-1]]:
                result1[i] = stack1[-1] - i
                stack1.pop()
            stack1.append(i)

        return result1
    
            
            
        
