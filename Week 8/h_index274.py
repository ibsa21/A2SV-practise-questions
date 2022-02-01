class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h_index += 1
        return h_index
        
