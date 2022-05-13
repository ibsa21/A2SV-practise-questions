class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        for v_one, v_two in zip_longest(v1, v2, fillvalue = 0):
            if v_one > v_two:return 1
            elif v_two > v_one:return -1
        return 0