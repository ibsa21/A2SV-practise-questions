class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        #keep the last index of every character
        last_index = {}
        
        #build last index dictionary
        for index, char in enumerate(s):
            last_index[char] = index
        
        left = 0
        right = 0
        
        partition_length = 0
        ans = []
        
        #iterate over the list
        for index, char in enumerate(s):
            
            partition_length += 1
            
            right = max(last_index[char], right)
            
            if index == right:
                ans.append(partition_length)
                partition_length = 0
        
        return ans