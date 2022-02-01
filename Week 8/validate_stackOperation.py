class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        newStack = []
        index = 0
        for i in range(len(pushed)):
            newStack.append(pushed[i])
            
            while newStack and newStack[-1]==popped[index]:
                newStack.pop()
                index += 1
                
        return index ==len(popped)
