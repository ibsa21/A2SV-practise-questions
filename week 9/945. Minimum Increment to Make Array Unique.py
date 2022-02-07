class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums or len(nums)==1:
            return 0
        
        result = 0
        nums.sort()
        
        left = 0
        max_number = nums[0] 
        for i in range(1, len(nums)):
            
            rightEl = nums[i]
            if rightEl <= max_number:
                result += max_number - nums[i] + 1
                rightEl = max_number + 1
                
            max_number = rightEl
        return result
                
    
    #Approach 2
    """
  Longer version of Approach 1
  In this case the number of moves is calculated using mathematical induction formula (n * n-1)//2
    """
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return 0
                
        list_nums = list(collections.Counter(nums).items())
        list_nums.sort()
        max_value = -1; 
        result = 0
        
        for i, j in list_nums:
            move_number = 0
            value = i
            
            if j > 1:
                move_number = (j * (j-1))//2
                value += j-1
                
            if  max_value >= i:
                value += ((max_value - i) + 1)
                move_number += ((max_value - i) + 1) * j
                
            max_value =value
            result += move_number
        return result
    
    #Approach 3
    """
        Searching increments inside hashed data
        Passed Test-case 55/63
    """
    class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        result = 0
        my_dict = collections.Counter(nums)
        second_dict = my_dict

        for value in my_dict.copy():
            x = value

            while my_dict[value] > 1 and  my_dict[x]:
                x += 1
                result += 1
                
                if x not in my_dict:
                    my_dict[x]  = 1
                    my_dict[value] -= 1
                    x = value
        return result
