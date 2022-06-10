class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        r = 0
        
        ans = 0
        visited = set()
        
        while r < len(s):
            
            if s[r] in visited:
                while s[r] in  visited:
                    visited.remove(s[l])
                    l +=1
                    
            visited.add(s[r])
            ans = max(ans, len(visited))
            r += 1
        return ans
            
            
            