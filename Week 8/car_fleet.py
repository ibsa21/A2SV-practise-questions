class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Approaches to solve this problem
            1. sort the position of cars a  in reverse order 
            2. create a stack that stores the time it takes the car to reach the target distance
            3. Since the cars are sorted in a decreasing order,  stack should keep 
               increasing monotonicity, the reason is if the time it takes to reach the destination for the next bus is smaller than the time it takes for the current bus, 
               there is definitely a fleet.
        """
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
