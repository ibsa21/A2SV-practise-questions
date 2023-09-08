class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        count_n  = []
        for i in edges:
            for k in i:
                count_n.append(k)
        count = Counter(count_n)
        
        
        for key in count:
            if count[key]==len(edges):
                return key