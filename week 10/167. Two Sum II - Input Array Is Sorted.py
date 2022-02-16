#approach 1 (using hash)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        target_map = {}
        for index, num in enumerate(numbers):
            diff = target - num
            if diff in target_map:
                return [target_map[diff] + 1, index + 1]
            target_map[num] = index
        return []
        
#approach 2(using two pointers approach)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return [left + 1, right + 1]
            
        return []
