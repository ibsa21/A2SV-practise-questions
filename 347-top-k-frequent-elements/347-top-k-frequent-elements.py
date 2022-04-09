class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)
        value_key = []
        
        for key in count_nums:
            value_key.append((count_nums[key], key))
        
        heapq._heapify_max(value_key)
        
        ans = []
        for i in range(k):
            ans.append(heapq._heappop_max(value_key)[1])
        
        return ans