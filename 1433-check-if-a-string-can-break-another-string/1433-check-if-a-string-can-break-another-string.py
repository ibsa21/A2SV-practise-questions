class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()
        
        not_s1 = False
        for i in range(len(s1)):
            if s1[i] < s2[i]:
                not_s1 = True
                break
        
        if not not_s1:
            return True
        
        for i in range(len(s2)):
            if s2[i] < s1[i]:
                return False
        
        return True