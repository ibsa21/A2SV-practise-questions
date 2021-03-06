class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        
        max_citations  = 0
        def binary_search(low, high):
            nonlocal max_citations
            
            if low > high:
                return
            
            mid = low + (high - low)//2
            number_papers = len(citations) - mid
            
            if citations[mid] >= number_papers:
                max_citations = max(max_citations, number_papers)
                binary_search(low, mid-1)
            else:
                binary_search(mid + 1, high)
                
        binary_search(0, len(citations)-1)
        return max_citations
        