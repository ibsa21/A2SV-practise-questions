class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        diff = abs(len(v1) - len(v2))
        if len(v1) > len(v2):v2.extend([0] * diff)
        elif len(v1) < len(v2):v1.extend([0] * diff)
            
        for i in range(min(len(v1), len(v2))):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0