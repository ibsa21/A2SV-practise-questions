class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        s = list(s)
        lastPos = {char:-1 for char in s}
        left = 0
        max_length = 0
        
        for idx, char in enumerate(s):
            if lastPos[char] >= left:
                max_length = max(max_length, idx - lastPos[char])
                left = lastPos[char] + 1
            lastPos[char]  = idx
            max_length = max(max_length, idx - left + 1)
            
        return max_length
