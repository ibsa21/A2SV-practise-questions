class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        
        answer = []
        for left, right in zip(l,r):
            array = sorted(nums[left:right+1])
            
            is_arithmetic = True
            diff = None
            
            for i in range(1, len(array)):
                if diff is None:
                    diff = array[i] - array[i-1]
                if array[i] - array[i-1] != diff:
                    is_arithmetic = False
                    break
            
            answer.append(is_arithmetic)
        
        return answer