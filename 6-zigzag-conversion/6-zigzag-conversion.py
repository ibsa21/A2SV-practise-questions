class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row_word = {i:[] for i in range(numRows)}
        i = 0
        while i < len(s):
            
            j, k = 0,numRows -2
            while i < len(s) and j < numRows:
                row_word[j].append(s[i])
                i += 1
                j += 1
            
            while i < len(s) and k > 0:
                row_word[k].append(s[i])
                i += 1
                k -= 1
                
        res = []
        for i in range(numRows):
            res.extend(row_word[i])
        return ''.join(res)