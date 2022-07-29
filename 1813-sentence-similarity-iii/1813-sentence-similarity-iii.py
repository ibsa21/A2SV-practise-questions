class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        
        # let's assume shortest is sentence 1
        s1 = s1.split()
        s2 = s2.split()
        
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        #find a point at which sentence1 differs from sentence 2 from left
        left = None
        for i in range(min(len(s1), len(s1))):
            if s1[i] != s2[i]:
                left = i
                break
        
        if left == None: return True
        if len(s1)==len(s2): return False
        
        i, right = -1, None
        while i >= -min(len(s1), len(s1)):
            if s1[i] != s2[i]:
                break
            i-= 1
        right = i
        return s1[:left] + s2[left:right + 1] + s1[left:right + 1] +s1[right + 1:]==s2
