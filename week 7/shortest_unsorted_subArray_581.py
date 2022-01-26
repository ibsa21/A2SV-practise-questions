class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        
        mono_stack = []
        smallest = len(nums)-1
        
        for i in range(len(nums)):
            while mono_stack and  nums[i] < nums[mono_stack[-1]]:
                smallest = min(smallest, mono_stack.pop())
            mono_stack.append(i)
            
        mono_stack = [len(nums)-1]
        largest = 0
        for i in range(len(nums)-2, -1, -1):
            while mono_stack and  nums[i] > nums[mono_stack[-1]]:
                largest = max(largest, mono_stack.pop())
            mono_stack.append(i)
        
        if largest == 0 and smallest ==len(nums)-1:
            return 0
        else:
            return largest-smallest + 1
        
