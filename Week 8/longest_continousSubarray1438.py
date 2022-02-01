class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        deque_Max, deque_Min = deque(), deque()
        result = 0
        left = 0
        
        for right in range(len(nums)):
            while deque_Max and nums[deque_Max[-1]] <= nums[right]:
                deque_Max.pop()
            while deque_Min and nums[deque_Min[-1]] >= nums[right]:
                deque_Min.pop()
            deque_Max.append(right)
            deque_Min.append(right)
            
            while nums[deque_Max[0]] - nums[deque_Min[0]] > limit:
                left += 1
                if deque_Max[0] < left: 
                    deque_Max.popleft()
                if deque_Min[0] < left:
                    deque_Min.popleft()
                    
            result = max(result, right - left + 1)
            
        return result
