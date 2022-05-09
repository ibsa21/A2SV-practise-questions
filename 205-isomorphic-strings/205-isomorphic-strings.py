class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st_interchange = {}
        ts_interchange= {}
        
        for a, b  in zip(s, t):
            replace_a = a in st_interchange and st_interchange[a] !=b
            replace_b = b in ts_interchange and ts_interchange[b] != a
            
            if replace_a or replace_b:
                return False
            
            st_interchange[a] = b
            ts_interchange[b] = a
                
        return True