class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3 = []
        for i in arr2:
            arr3  += [i] * arr1.count(i)
            
        arr4 = []
        for i in arr1:
            if i not in arr2:
                arr4.append(i)
                
        arr4.sort()
        arr3+= arr4
        arr1 = arr3
        return arr3
