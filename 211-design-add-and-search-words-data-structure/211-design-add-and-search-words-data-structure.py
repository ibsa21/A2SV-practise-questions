class TrieNode:
    def __init__(self, char = ''):
        self.children  = {}
        self.char = char
        self.isEnd = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)
            root = root.children[char]
        root.isEnd = True
    
    def dfs(self, i, word, root):
        if i >=len(word):
            return root.isEnd
        if word[i] == '.':
            for child in root.children:
                if self.dfs(i + 1, word, root.children[child]):
                    return True
        else:
            if word[i] not in root.children:return False
            if self.dfs(i + 1, word, root.children[word[i]]): return True
        return False

    def search(self, word: str) -> bool:
        root = self.root
        for idx, char in  enumerate(word):
            if char == '.':
                # print(word[idx + 1:], word)
                return self.dfs(idx, word, root)
                
            if char not in root.children:
                return False
            root = root.children[char]
        return root.isEnd
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)