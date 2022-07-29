class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        
        # let's assume shortest is sentence 1
        s1 = s1.split()
        s2 = s2.split()
        
        if len(s1) > len(s2):
            s1, s2 = s2, s1
            
        #take the longest prefix
        left = 0
        while left < len(s1) and s1[left]==s2[left]:
            left += 1
        
        if left==len(s1): return True
        #take the longest suffix
        right = -1
        while right >= -len(s1) and s1[right]==s2[right]:
            right-= 1
        if right + 1==0: right = len(s1)
        
        return s1[:left] + s2[left:right + 1] + s1[left:right + 1] +s1[right + 1:]==s2
