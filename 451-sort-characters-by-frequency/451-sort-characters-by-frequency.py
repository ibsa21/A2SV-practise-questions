class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        
        sorted_list = []
        for key in count:
            heapq.heappush(sorted_list, (-count[key], key))
        result = ''
        while sorted_list:
            cur_char = heapq.heappop(sorted_list)
            result += (cur_char[1] * -cur_char[0])
        return result