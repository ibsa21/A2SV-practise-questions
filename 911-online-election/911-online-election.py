class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.winner = {}
        self.counter = {}
        
        max_person = (0, None)
        
        def find_dictValue(item):
            for key in self.counter:
                if key==item:
                    return self.counter[key]
            return 0
    
        for i in range(len(self.times)):
            p = persons[i]
            
            self.counter[p] = find_dictValue(p) + 1
            
            if self.counter[p]>=max_person[0]:
                max_person = (self.counter[p], p)
                
            self.winner[i]=max_person[1]

    def q(self, t: int) -> int:
    
        best = 0
        
        def binary_search(low, high):
            
            nonlocal best
            
            if low > high:
                return best
            
            mid = low + (high-low)//2
            
            if self.times[mid] == t:
                return mid
            
            elif self.times[mid] < t:
                best = mid
                return binary_search(mid + 1, high)
            else:
                return binary_search(low, mid-1)
            
        return self.winner[binary_search(0, len(self.times)-1)]
    
        
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)