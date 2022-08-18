class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = [0] * (max(arr) + 1)
        for idx, value in enumerate(arr):
            counter[value] += 1
            
        counter.sort(reverse = True)
        count_sum = 0
        for idx, value in enumerate(counter):
            count_sum += value
            if count_sum >= len(arr)//2:
                return idx + 1
        
        
        