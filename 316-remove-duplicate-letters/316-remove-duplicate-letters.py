class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        letter_count = Counter(s)
        mono_stack  = []
        visited = set()
        
        for i in range(len(s)):
            
            if s[i] in visited:
                letter_count[s[i]] -= 1
            else:
                while mono_stack and s[mono_stack[-1]] >= s[i] and letter_count[s[mono_stack[-1]]] > 1:
                    removed = mono_stack.pop()
                    letter_count[s[removed]] -= 1

                    visited.remove(s[removed])
            
                mono_stack.append(i)
                visited.add(s[i])
                
        
        return ''.join([s[i] for i in mono_stack])
