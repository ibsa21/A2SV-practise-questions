class TrieNode:
    
    def __init__(self, folder_name = ''):
        self.children = {}
        self.end_folder = False
        self.char = folder_name

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        #build a trie data structure
        trie_node  = TrieNode()
        
        #def build_trie(trie_data):
            
        for directory in folder:
            trie_data = trie_node
            directory = directory.split('/')

            for char in directory[1:]:
                if char not in trie_data.children:
                    trie_data.children[char] = TrieNode(char)

                trie_data = trie_data.children[char]
            trie_data.end_folder = True
            
        
        result = []
        
        def dfs(trie_node, folder):
            nonlocal result
            
            if not trie_node:return 
            
            if trie_node.char != '':
                folder += '/'
                folder += trie_node.char
            
            if trie_node.end_folder:
                return folder
            
            for sub_dir in trie_node.children:
                result_folder = (dfs(trie_node.children[sub_dir], folder))
                
                if result_folder:
                    result.append(result_folder)
        
        dfs(trie_node, '')
        return result