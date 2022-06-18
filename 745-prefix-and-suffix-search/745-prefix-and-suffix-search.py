class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_index = -1

class WordFilter:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        
        for idx, word in enumerate(words):
            cur_suffix = ""
            for char in word[::-1]:
                cur_suffix += char
                self.insert(cur_suffix + "#" + word, idx)
        
    def insert(self, word, idx):
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur.end_index  = idx
            cur = cur.children[char]

        cur.end_index = idx
            
    def search(self, word, root):
        for char in word:
            if char not in root.children:
                return -1
            root = root.children[char]
        return root.end_index
    
    def f(self, prefix, suffix):
        
        return self.search(suffix[::-1] + "#" + prefix, self.root)