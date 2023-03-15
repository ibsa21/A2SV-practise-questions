class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        indexMapper = {val:idx for idx, val in enumerate(arr)}
        
        def reverse(left, right):
            while left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                indexMapper[arr[left]] = left
                indexMapper[arr[right]] = right
                left += 1
                right -= 1
                
        val = n
        answer = []
        while val > 0:
            
            idx = indexMapper[val]
            
            if idx == val-1:
                val -= 1
            else:
                if idx == 0:
                    answer.append(val)
                    reverse(0, val-1)
                    val -= 1
                else:
                    answer.append(idx+1)
                    reverse(0, idx)
                    
        return answer