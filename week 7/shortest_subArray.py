class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        """
        case for this problem:
            1.sum number that is greater than or equal to k will only be achieved at the last index
            2. there is no number that can add up to k
            3. subArray of length s that can add up to greater than or equal to k is contagious somewhere
            4. We only have one number that is sufficient for the condition
        
        """
        mono_queue = collections.deque()
        sumValue = 0
        smallest = 100001;
        
        for i in range(len(nums)):
            
            sumValue += nums[i]
            if sumValue >= k:
                smallest = min(smallest, i + 1)
            
            #if this condition is not met there is always more than 1 elements that can add up to k
            if nums[i]==k:
                return 1
            else:
                
                #keeping monotonic increasing of stack - last-in first-out
                while mono_queue and  sumValue <= mono_queue[-1][0]:
                    mono_queue.pop()
                
                #increasing monotonic_queue first-in first-out
                while mono_queue and  sumValue - mono_queue[0][0] >= k:
                    smallest = min(smallest, mono_queue[-1][1]- mono_queue.popleft()[1] + 1)
                    
                mono_queue.append([sumValue, i])
                
        return -1 if smallest ==100001 else smallest
                
                
                
            
