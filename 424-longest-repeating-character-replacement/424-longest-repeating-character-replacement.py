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
        
        def sum_charFreq():
            sum_value = 0
            
            for key in char_freq:
                sum_value += char_freq[key]
                
            return sum_value
        
        max_len = 0
        left = 0
        right = 0
        k_count = k
        
        while right < len(s):
            
            char_freq[s[right]] += 1
            
            if sum_charFreq() - find_maxChar() <= k:
                max_len = max(max_len, right - left + 1)
            else:
                char_freq[s[left]] -= 1
                left += 1
            
            right +=1
        
        return max_len
                
            
            