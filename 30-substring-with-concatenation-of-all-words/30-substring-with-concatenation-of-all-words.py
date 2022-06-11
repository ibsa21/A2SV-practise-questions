class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        l = len(words[0]) * len(words)
        n = len(words[0])
        
        def isValid(i, k, n, words):
            for j in range(i, k, n):
                word = s[j:j + n]
                if word not in words:
                    return False
                words[word]-=1
                if words[word] == 0:
                    del words[word]
            return True
        
        ans = []
        for i in range(len(s)-l + 1):
            word_set = Counter(words)
            if isValid(i, i + l, n, word_set):
                ans.append(i)
        return ans
