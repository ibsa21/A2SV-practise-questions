class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        K_count = k
        count_occur = Counter(words)
        
        key_value = []
        for key in count_occur:
            key_value.append([-1 * count_occur[key], key])
        heapq.heapify(key_value)
        return [heapq.heappop(key_value)[1] for _ in range(k)]
        