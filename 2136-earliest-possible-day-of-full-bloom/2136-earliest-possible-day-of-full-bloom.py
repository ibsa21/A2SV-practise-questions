class Solution:
    def earliestFullBloom(self, p: List[int], g: List[int]) -> int:

        a = sorted(list(zip(g,p)), reverse = True)
        
        lbd = 0
        free = 0
        
        for gt, pt in a:
            
            if free < pt:
                lbd += gt+pt-free
                free = gt
            else:
                free -= pt
                
                if free < gt:
                    lbd += gt-free
                    free = gt
        return lbd