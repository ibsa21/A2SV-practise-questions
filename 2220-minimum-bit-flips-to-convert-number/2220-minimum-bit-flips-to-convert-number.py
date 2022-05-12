class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a, b = bin(start), bin(goal)
        i,j, ans = len(a)-1, len(b)-1, 0
        while max(i, j) > -1:
            x = int(a[i]) if i >= 0 and a[i] != 'b' else 0
            y = int(b[j]) if j  >= 0 and b[j] != 'b' else 0
            
            if x != y:ans += 1
            if i >= 0: i -=1
            if j >= 0: j -=1
        return ans