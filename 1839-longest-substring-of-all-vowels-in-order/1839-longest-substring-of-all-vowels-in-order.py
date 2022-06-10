class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        stack = []
        mydict = {'a':1, 'e':2, 'i':3, 'o':4, 'u':5}
        
        ans = 0
        for i, char in enumerate(word):
            if stack and  char == word[stack[-1][0]]:
                continue
                
            if not stack:
                if mydict[char] ==1:
                    stack.append((i, mydict[char]))
            else:
                if mydict[char] != stack[-1][1] + 1:
                
                    if len(stack) == 5:
                        ans = max(ans, i - stack[0][0])
                        
                    stack = []
                    
                    if mydict[char] ==1:
                        stack.append((i, mydict[char]))
                else:
                    stack.append((i, mydict[char]))
        if len(stack) == 5:
            ans  = max(ans, len(word) - stack[0][0])
        return ans
                