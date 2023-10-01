class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # if ith of current state is that means ith value is not inside sliding window
        current_state = defaultdict(int)
        
        left_idx = 0
        answer = []
        heap = []
        for right_idx, num in enumerate(nums):
            current_state[num] += 1
            heapq.heappush(heap, -num)
            if right_idx - left_idx + 1 == k:
                while current_state[-heap[0]] == 0:
                    left_number = -heapq.heappop(heap)
                    if current_state[left_number] > 0:
                        current_state[left_number] -= 1
                answer.append(-heap[0])
                if current_state[nums[left_idx]] > 0:
                    current_state[nums[left_idx]] -= 1
                left_idx += 1
        return answer