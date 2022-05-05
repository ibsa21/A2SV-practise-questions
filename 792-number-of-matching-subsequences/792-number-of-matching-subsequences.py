class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = 0     
    
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        root = TrieNode()
        
        #build trie data structure
        for word in words:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.ends += 1
        
        
        count = 0
        def dfs(key, node, i):
            
            nonlocal count
            if not node:return
            
            #determine whether subsequence is valid or not
            while i < len(s) and s[i] != key:
                i +=1
            
            #subsequence valid
            if i < len(s):
                count += node.ends
                for key,child in node.children.items():
                    dfs(key,child, i+1)
        
        for key,value in root.children.items():
            dfs(key,value, 0)
        return count