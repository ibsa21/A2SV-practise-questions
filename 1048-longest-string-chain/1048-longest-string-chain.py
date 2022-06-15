class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        longest_string_chain, len_words = 1, len(words)
        
        # tabulation
        dp = defaultdict(int)
        
        #sorting based on the length of the words
        words = sorted(words, key = lambda x: len(x))
        for word in words:
            dp[word] = 1
            prev_chain = [word[:i] + word[i + 1:] for i in range(len(word))]
            for prev_word in prev_chain:
                if prev_word in dp: 
                    dp[word] = dp[prev_word] + 1
                    longest_string_chain = max(longest_string_chain, dp[word])
        
        return longest_string_chain