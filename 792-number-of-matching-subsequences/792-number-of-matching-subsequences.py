class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = 0     
    
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        root = TrieNode()
        for word in words:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
            cur.ends += 1
        
        count = 0
        def dfs(k,node, i):
            nonlocal count
            if not node:return
            
            while i < len(s):
                if s[i] == k:
                    break
                i +=1
                
            if i < len(s):
                count += node.ends
                for k,child in node.children.items():
                    dfs(k,child, i+1)
        
        for k,v in root.children.items():
            dfs(k,v,0)
        return count