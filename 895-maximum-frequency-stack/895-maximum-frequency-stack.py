class FreqStack:

    def __init__(self):
        self.stack = [[None] for i in range(2 * 10**4)]
        self.freq_map = defaultdict(int)
        self.mf = 0

    def push(self, val: int) -> None:
        
        self.freq_map[val] += 1
        self.stack[self.freq_map[val]-1].append(val)
        self.mf = max(self.mf, self.freq_map[val])
        
    def pop(self) -> int:
        
        if len(self.stack[self.mf-1])==1:
            self.mf -= 1
        
        res = self.stack[self.mf-1].pop()
        self.freq_map[res]-= 1
        return res                
            


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()