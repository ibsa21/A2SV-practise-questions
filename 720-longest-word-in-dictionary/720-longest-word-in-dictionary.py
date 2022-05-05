class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.end = False
    
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie_data = TrieNode()
        
        #building trie data
        for word in words:
            root  = trie_data
            for char in word:
                if char not in root.children:
                    root.children[char]  = TrieNode()
                
                root = root.children[char]
            
            root.end = True
        
        result = ''
        def dfs(trie, string, char):
            nonlocal result
            
            if trie.end:string += char    
            else:return string
                
            if not trie.children: return string
            
            for child_trie in trie.children:
                res_string = dfs(trie.children[child_trie], string, child_trie)
                
                if res_string:
                    if len(res_string) == len(result):
                        result = min(res_string, result)
                    else:
                        result = res_string if len(res_string ) > len(result) else result
        
        for node in trie_data.children:
            dfs(trie_data.children[node], '', node)
        return result
                             
        