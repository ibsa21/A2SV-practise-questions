class TrieNode:
    
    def __init__(self, char = ''):
        self.children = {}
        self.end_word = False
        self.char = char
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.memo = {}
    
    def add_word(self, word):
        root = self.root
        
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)
            
            root = root.children[char]
        
        root.end_word = True
        
    
    def search_word(self, word):
        
        heap = []
        def dfs(root, string):
            nonlocal heap
            
            string += root.char
            
            if not root:
                return string
            
            if root.end_word:
                heapq.heappush(heap, string)
                
            for child in root.children:
                
                string_value = dfs(root.children[child], string)
                if string_value:
                    heapq.heappush(heap, string_value)
                
        root = self.root
        result = []
        str_now = ''
        for i in range(len(word)):
            char  = word[i]
            
            if char not in root.children:
                result.extend([[]] * (len(word) - i))
                return result
            
            root = root.children[char]
            dfs(root, str_now)
            str_now += char
            result.append(heapq.nsmallest(3, heap))
            heap  = []
            
        return result
            
            
        
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products_trie = Trie()
        
        for product in products:
            products_trie.add_word(product)
        
        
        return products_trie.search_word(searchWord)
        
        