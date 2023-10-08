class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()

        for h_index in range(max(citations), -1, -1):
            pos = bisect_left(citations, h_index)
            if len(citations)-pos >= h_index:
                return h_index
        
        return 0