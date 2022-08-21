from collections import OrderedDict
class Solution:
    def canBeReplaced(self,stamp:str,target:str, idxPos:int)->bool:
        for i, char in enumerate(stamp):
            if target[i + idxPos] != '?' and target[i + idxPos] != char:
                return False
        return True
    
    def replace(self, istart:int, iend:int, target:str, idx_pos:int)->int:
        for idx in range(istart, iend):
            if target[idx] != '?':
                idx_pos += 1
                target[idx] = '?'
        return idx_pos
        
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target = list(target)
        replaced_idx = OrderedDict()

        idx_pos = 0
        while idx_pos != len(target):
            is_changed = False
            for i in range(len(target)-len(stamp) + 1):
                if i not in replaced_idx and self.canBeReplaced(stamp, target, i):
                    idx_pos = self.replace(i, i + len(stamp), target, idx_pos)
                    replaced_idx[i] = None
                    is_changed = True
                    
                    if idx_pos == len(target):
                        break
            if is_changed is False:
                return []
            
        result = [key for key in replaced_idx]
        return result[::-1]
        