class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set(list("qwertyuiop"))
        row2 = set(list("asdfghjkl"))
        row3 = set(list("zxcvbnm"))
        
        def isValid(word, given_set):
            for char in word:
                if char.lower() not in given_set:
                    return False
            
            return True
        
        
        ans  = []
        
        for word in words:
            
            
            if isValid(word, row1) or isValid(word, row2) or isValid(word, row3):
                ans.append(word)
            
            
        return ans