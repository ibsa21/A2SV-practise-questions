class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        
        #dynamic programming + tabulation O(N) space and time complexity
        table = [[0, i] for i in range(len(word), 0,-1)]
        table[-1][0] =1 if word[-1] in  vowels else 0
        
        for i in range(len(word)-2, -1, -1):
            
            if word[i] in vowels:
                table[i][0]  = 1 + sum(table[i+1])
            else:
                table[i][0] = table[i+1][0]

        return sum([x for x, y in table])