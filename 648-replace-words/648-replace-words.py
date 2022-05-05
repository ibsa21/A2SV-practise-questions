class TrieNode:
    def __init__(self, char = ''):
        self.children = {}
        self.end_word =False
        self.char = char
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        trie  = TrieNode()
        
        for word in dictionary:
            root =trie
            for char in word:
                if char not in root.children:
                    root.children[char] =  TrieNode(char)
                root = root.children[char]
            root.end_word = True
        
        
        def search_word(word, trie):
            str_now = ''
            for char in word:
                if trie.end_word:
                    return str_now
                if char not in trie.children:
                    return word
                trie = trie.children[char]
                str_now += trie.char
            return str_now
        
        result = ''
        for word in sentence.split():
            result += search_word(word, trie)
            result += ' '
        
        return result[:-1]