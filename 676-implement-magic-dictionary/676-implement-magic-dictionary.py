class MagicDictionary:

    def __init__(self):
        self.dictionary = defaultdict(list)
        
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            n = len(word)
            self.dictionary[n].append(word)
            
    def isEqaul(self,searchWord, word):
        len_word,number_changes = len(word), 0
        for idx in range(len_word):
            if searchWord[idx] != word[idx]:
                number_changes += 1
                if number_changes > 1: return False
        return False if number_changes == 0 else True
    
    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        for word in self.dictionary[n]:
            if self.isEqaul(searchWord, word): return True
        return False
    
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)