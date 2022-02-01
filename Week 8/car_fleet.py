class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append([position[i], speed[i]])
            
        pos_speed.sort()
        
        stack = []
        for pos, speed in pos_speed[::-1]:
            stack.append((target-pos)/speed)
            
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)
