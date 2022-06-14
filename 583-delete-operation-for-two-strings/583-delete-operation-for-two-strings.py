class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        table = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if word1[i]==word2[j]:
                    table[i+1][j+1] = 1 + table[i][j]
                else:
                    table[i+1][j+1] = max(table[i][j+1], table[i+1][j])

        longest_common_subsequence = table[-1][-1]		
        return m + n - (2 * longest_common_subsequence)