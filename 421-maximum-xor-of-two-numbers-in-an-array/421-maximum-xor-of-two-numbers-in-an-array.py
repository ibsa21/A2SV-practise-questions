class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.num = -1
        
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        
        for num in nums:
            cur_root = root
            for i in range(31, -1, -1):
                node = num & (1<<i)
                node = 1 if node >0 else 0
                if not cur_root.children[node]:
                    cur_root.children[node] = TrieNode()
                cur_root = cur_root.children[node]
            cur_root.num = num
        
        def findHighest(num):
            cur_root = root
            for i in range(31, -1, -1):
                node = num & (1<<i)
                node = 1 if not node else 0
                
                if cur_root.children[node]:
                    cur_root = cur_root.children[node]
                else:
                    cur_root = cur_root.children[int(not node)]
            
            return num ^ cur_root.num
        max_or = 0
        for num in nums:
                max_or = max(max_or, findHighest(num))
        return max_or