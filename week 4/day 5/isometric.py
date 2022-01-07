class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st_interchange = {}
        ts_interchange= {}
        for a, b  in zip(s, t):
            if ((a in st_interchange and st_interchange[a] != b) or (b in ts_interchange and ts_interchange[b] != a)):
                return False
            st_interchange[a] = b
            ts_interchange[b] = a
                
        return True
    
