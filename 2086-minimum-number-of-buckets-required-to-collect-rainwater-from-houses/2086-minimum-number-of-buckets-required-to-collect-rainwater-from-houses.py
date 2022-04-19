class Solution:
    def minimumBuckets(self, street: str) -> int:
        
        if len(street) == 1:
            if street[0] == 'H':
                return -1
            else:
                return 0
            
        street = list(street)
        def helper_choose(i):
            
            if i -1 < 0:
                return i + 1 if  street[i + 1] in ('B', '.') else "IMPOSSIBLE"
            elif i + 1 >= len(street):
                return i - 1 if street[i -1] in ('B', '.') else "IMPOSSIBLE"
            else:
                left_found = street[i -1] in ('B', '.')
                right_found = street[i + 1] in ('B', '.')
                
                if street[i-1] == 'B':
                    return i -1
                elif street[i + 1] == 'B':
                    return i + 1
                elif left_found and right_found or right_found:
                    return i + 1
                elif left_found:
                    return i - 1
                else:
                    return "IMPOSSIBLE"
            
        count = 0
        for i in range(len(street)):
            
            if street[i] == 'H':
                value = helper_choose(i)
                print(value, i)
                if value != "IMPOSSIBLE":
                    
                    if  street[value] == '.':
                        count += 1
                        street[value] = 'B'
                else:
                    return -1
                
        return count