class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        s.sort(key = self.sort_by_last)
        
        newStr = ""
        for str in s:
            newStr += (str[:-1] + " ")
        return newStr.rstrip()
        
    def sort_by_last(self, s):
        return s[-1]
        
