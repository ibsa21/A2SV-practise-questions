class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        incoming_edge = set()
        for source, dest in edges:
            incoming_edge.add(dest)
        
        return set([source for source, dest in edges if source not in incoming_edge])
            
            