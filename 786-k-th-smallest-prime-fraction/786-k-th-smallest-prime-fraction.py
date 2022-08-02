from sortedcontainers import SortedList
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        # bruteforce
        sorted_list = []
        for idx, num in enumerate(arr):
            for j, second_num in enumerate(arr[idx + 1:]):
                sorted_list.append((num/second_num, (num, second_num)))
        
        sorted_list.sort()
        return sorted_list[k-1][1]
                
        