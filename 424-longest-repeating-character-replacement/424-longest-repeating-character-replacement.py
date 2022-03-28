class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        char_freq = {}
        for char in s:
            char_freq[char] = 0
        
        def find_maxChar():
            max_freq = 0
            
            for key in char_freq:
                if char_freq[key] >= max_freq:
                    max_freq = char_freq[key]
            return max_freq
        
        
        max_len = 0
        left = 0
        right = 0
        
        sum_frequency  = 0
        max_curr_freq = 0
        while right < len(s):
            
            char_freq[s[right]] += 1
            sum_frequency += 1
            
            if char_freq[s[right]] >= max_curr_freq:
                max_curr_freq = char_freq[s[right]]
                
            if sum_frequency - max_curr_freq <= k:
                max_len = max(max_len, right - left + 1)
            else:
                char_freq[s[left]] -= 1
                sum_frequency -= 1
                left += 1
            
            right +=1
        
        return max_len