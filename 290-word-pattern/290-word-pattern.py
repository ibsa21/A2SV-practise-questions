class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        match_pattern = {}
        s = s.split()
        
        if len(set(s)) < len(set(pattern)) or len(pattern) < len(s):return False
        for i in range(len(pattern)):
            char = pattern[i]
            if char in match_pattern and match_pattern[char] != s[i]:
                return False
            match_pattern[char] = s[i]
        return True