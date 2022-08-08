class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        my_dict = {}
        for i in range(len(arr)-1, -1, -1):
            if arr[i] + difference not in my_dict:
                my_dict[arr[i]] = 1
            else:
                my_dict[arr[i]] = my_dict[arr[i] + difference] + 1
        return max([value for key, value in my_dict.items()])
