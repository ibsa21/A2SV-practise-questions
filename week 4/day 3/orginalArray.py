class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        length = len(changed)
        if(length %2 == 1):
            return []
        
        number_count = Counter(changed)
        result = []
        print(number_count)
        for i in sorted(changed):
            
            if i==0 and number_count[i] >=2:
                number_count[i] -= 2
                result.append(i)
            elif i > 0 and number_count[i] and number_count[i*2]:
                number_count[i] -=1
                number_count[i*2] -=1
                result.append(i)
                
        if len(result) == length//2:
            return result
        else:
            return []
