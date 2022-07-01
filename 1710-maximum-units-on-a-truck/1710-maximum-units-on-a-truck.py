class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        cur_size =0
        total_unit = 0
        i = 0
        while i < len(boxTypes) and  cur_size < truckSize:
            num, unit = boxTypes[i]
            if cur_size + num > truckSize:
                total_unit += (unit * (truckSize - cur_size))
                return total_unit
            cur_size += num
            total_unit += (num * unit)
            i += 1
        return total_unit
        
                
                