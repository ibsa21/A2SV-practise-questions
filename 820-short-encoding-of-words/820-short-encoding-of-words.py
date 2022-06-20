class TrieNode:
    def __init__(self, word = ''):
        self.children ={}
        self.end_suffix = False
    
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        #solution 1
        prefix_dictionary = set()
        shortest_encoding_length  = 0
        
        #let's sort the words based on their length
        words = sorted(words, key =  lambda x: len(x))
        
        #build trie node
        for word in words[::-1]:
            
            if word not in prefix_dictionary :
                shortest_encoding_length += (len(word) + 1)
            cur_suffix = ''
            for idx, char in enumerate(word[::-1]):
                cur_suffix = char + cur_suffix
                prefix_dictionary.add(cur_suffix)
        return shortest_encoding_length
        
        #solution 2
        #let's build a trie node
        root = TrieNode()
        
        def insert(word):
            cur_root = root
            for char in word:
                if char not in cur_root.children:
                    cur_root.children[char]  = TrieNode(word)
                
                cur_root = cur_root.children[char]
            cur_root.end_suffix = True
            return
        
        def search(word):
            cur_root = root
            for char in word:
                if char not in cur_root.children:
                    return False
                cur_root= cur_root.children[char]
            return cur_root.end_suffix
                
        shortest_encoding_length  = 0
        
        #let's sort the words based on their length
        words = sorted(words, key =  lambda x: len(x))
        
        #build trie node
        for word in words[::-1]:
            
            if not search(word):
                shortest_encoding_length += (len(word) + 1)
            cur_suffix = ''
            for idx, char in enumerate(word[::-1]):
                cur_suffix = char + cur_suffix
                insert(cur_suffix)
        return shortest_encoding_length