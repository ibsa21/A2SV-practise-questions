class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        
        def is_match(word:str, pattern:str):
            direct_map = {}
            reverse_map  = {}
            for char1, char2 in zip_longest(word, pattern, fillvalue = None):
                if char2 in direct_map and direct_map[char2] != char1: return False
                if char1 in reverse_map and reverse_map[char1] != char2: return False
                direct_map[char2] = char1
                reverse_map[char1] = char2
            return True
        
        result = []
        for word in words:
            if is_match(word, pattern):
                result.append(word)
        return result
        