class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        my_dict = OrderedDict()
        
        
        left = 0
        right = 10
        
        while right < len(s):
            key = s[left:right]
            
            if key in my_dict:
                my_dict[key] += 1
            else:
                my_dict[key] = 1
                
            right += 1
            left += 1
        
        if s[left:right] in my_dict:
            my_dict[s[left:right]] += 1
            
        return [key for key in my_dict if my_dict[key] > 1]