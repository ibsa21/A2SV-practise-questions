class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        root = TrieNode()
        for word in words:
            curRoot = root
            for char in word:
                if char not in curRoot.children:
                    curRoot.children[char]  = TrieNode()
                curRoot = curRoot.children[char]
            curRoot.isEnd = True
        
        words.sort()
        
        def search(word):
            cur_root = root
            for char in word:
                
                if char not in cur_root.children or cur_root.children[char].isEnd is False:
                    return False
                cur_root = cur_root.children[char]
            return cur_root.isEnd
        
        ans = ''
        for word in words:
            if search(word) and len(word) > len(ans):
                ans = word
        return ans