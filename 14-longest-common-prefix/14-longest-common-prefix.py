class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        word = strs[0]
        
        a = 0
        for i in range(len(word)):
            char = word[i]
            
            for k in range(len(strs)):
                if a >= len(strs[k]) or  strs[k][a] != char:
                    return word[:a]
            a += 1
        return word[:a]
            