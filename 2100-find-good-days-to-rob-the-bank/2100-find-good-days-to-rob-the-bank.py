class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        if time==0:
            return [i for i in range(len(security))]
        
        #approach number one - time-complexity O(N), space-complexity O(N)
        left_goodday, left = [0 for i in range(len(security))], 1
        right_goodday, right = [0 for i in range(len(security))], len(security) -2
        
        
        #one-time from left
        robbing_day = 0
        while left < len(security):
            
            if security[left] <= security[left -1]:
                left_goodday[left] = 1  + left_goodday[left -1]
            
            left += 1
        
        while right > -1:
            
            if security[right] <= security[right + 1]:
                right_goodday[right] = 1 + right_goodday[right + 1]
            right -= 1
    
        
        return [ i for i in range(len(security)) if right_goodday[i] >=time and left_goodday[i] >= time]
            
        
        #second approach - not so eficient
        def in_range(i):
            return i - time >= 0 and len(security) - time > i
        
        while left < len(security):
            
            if in_range(left):
                is_goodday = True
                for i in range(left - time + 1, left + 1):
                    if security[i] > security[i - 1]:
                        is_goodday = False
                        
                if is_goodday:
                    for i in range(left + 1, left + time + 1):
                        if security[i] < security[i -1]:
                            is_goodday = False
                            
                if is_goodday:
                    result.append(left)
            left += 1
        
        return result
                