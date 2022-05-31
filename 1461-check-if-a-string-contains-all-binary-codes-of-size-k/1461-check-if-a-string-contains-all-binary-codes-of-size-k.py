class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        combination = pow(2, k)        
        taken_combination = set()
        
        for i in range(k, len(s)+1):
            
            tmp = s[i-k:i]
            if tmp not in taken_combination:
                
                taken_combination.add(tmp)
                combination -= 1
                
                if combination == 0:
                    return True
        return False